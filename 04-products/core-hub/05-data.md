---
title: "Core Hub — Data Model & Governance"
status: draft
owners:
  - Gabriel
updated: 2026-01-16
links:
  - /docs/03-products/core-hub/01-prd.md
  - /docs/03-products/core-hub/02-spec.md
  - /docs/03-products/core-hub/03-architecture.md
  - /docs/03-products/core-hub/04-api.md
  - /docs/03-products/core-hub/06-llmops.md
  - /docs/00-index/decision-log.md
tags:
  - data
  - governance
  - core-hub
  - ia-first
---

## Contexto
Modelo de dados, governança e retenção do Core Hub para suportar MVP (piloto assistido, 1 fluxo) e v1 (multi-tenant com 2–3 fluxos).

## Objetivo
Definir entidades, relacionamentos, constraints, índices e políticas de retenção/segurança para implementação e operação segura (LGPD).

## Escopo
- Esquema relacional (PostgreSQL) + vector store (Qdrant) + storage (S3/MinIO).
- Tabelas principais de negócio, auditoria e configurações.
- Retenção, PII, minimização, encriptação e mask.

## Não-escopo
- Modelagem de BI/dashboards avançados.
- Esquemas de billing internos.

---

## 1) Entidades principais (PostgreSQL)

| Tabela | Descrição | Campos chave |
|--------|-----------|--------------|
| tenants | Cliente/instância | id (uuid PK), name, status |
| users | Usuários | id, tenant_id FK, email (unique per tenant), role, name, password_hash, mfa_enabled |
| roles | Perfis | role (admin/operator/viewer), permissions (jsonb) |
| integrations | Conexões externas | id, tenant_id, type (erp/email/bank/chat), provider, status, credentials_ref |
| flows | Configuração de fluxo | id, tenant_id, type (cobranca/conciliacao/pagamento), config jsonb, require_approval bool |
| cobrancas | Cobranças geradas | id, tenant_id, fatura_ref, cliente_ref, valor numeric, vencimento date, status, confidence numeric, message jsonb |
| conciliacoes | Execuções de conciliação | id, tenant_id, conta_ref, periodo, status, resumo jsonb |
| conciliacao_divergencias | Divergências detectadas | id, conciliacao_id FK, tipo, sugestao jsonb, status, confidence |
| pagamentos | Boletos/AP | id, tenant_id, cedente, valor, vencimento, status, classificacao jsonb, confidence |
| approvals | Itens de HIL | id, tenant_id, entity_type, entity_id, status, approved_by, comment |
| audit_logs | Eventos auditáveis | id, tenant_id, user_id, action, entity_type, entity_id, payload jsonb, confidence, ip, created_at |
| configs | Configurações gerais | tenant_id PK, cobranca jsonb, conciliacao jsonb, pagamento jsonb |
| files | Arquivos (boletos, extratos) | id, tenant_id, path, type, checksum, size, created_at |

### Índices e constraints
- `users(email, tenant_id)` unique.
- `cobrancas(tenant_id, status, vencimento)` btree.
- `conciliacao_divergencias(conciliacao_id, status)` btree.
- `approvals(tenant_id, status, created_at)` btree.
- `audit_logs(tenant_id, entity_type, entity_id)` btree; `created_at` index para ordenação.
- FK com `ON DELETE CASCADE` para dados dependentes de tenant.

### Integridade e validade
- Valores monetários: numeric(14,2), `CHECK valor > 0`.
- Status com `CHECK` enumerado por fluxo.
- Timestamps em UTC.

---

## 2) Vetores (Qdrant)

| Coleção | Conteúdo | Observações |
|---------|----------|-------------|
| `kb_chunks` | Embeddings de documentos (FAQ, políticas) | Por tenant; payload inclui `source`, `doc_id`, `version`, `tenant_id` |
| `ledger_chunks` [OPEN] | Chunks de extratos/lançamentos para conciliação assistida | Validar necessidade no MVP |

- Dimensão: 1536 (text-embedding-3-small).  
- Sharding: 1 shard (MVP), replicação 1.  
- Filtros obrigatórios por `tenant_id`.

---

## 3) Storage (S3/MinIO)

| Bucket/prefixo | Conteúdo | Criptografia | Retenção |
|----------------|----------|--------------|----------|
| `tenants/{tenant_id}/files/boletos/` | PDFs de boletos | SSE | 180 dias |
| `tenants/{tenant_id}/files/extratos/` | OFX/CSV | SSE | 180 dias |
| `tenants/{tenant_id}/exports/` | Exports solicitados | SSE | 7 dias |

---

## 4) Retenção e purge

| Dado | Retenção | Purge |
|------|----------|-------|
| Dados operacionais (cobrancas, conciliacoes, pagamentos) | 24 meses [OPEN] | Soft delete + purge trimestral |
| Audit logs | 5 anos | Append-only; purge após expirar |
| Arquivos (boletos/extratos) | 180 dias | Deletar + remover referências |
| Tokens de refresh | 7 dias | Revogar em logout/comprometimento |
| Embeddings | 24 meses ou ao remover fonte | Deletar vetores do tenant |

---

## 5) PII, minimização e LGPD

| Categoria | Exemplo | Tratamento |
|-----------|---------|------------|
| Identificadores pessoais | nome, e-mail, telefone | Criptografia em trânsito; em repouso no DB; mask em logs |
| Financeiros sensíveis | valores de faturas/pagamentos | Sem mask no DB (necessário ao fluxo), mask em logs/export; acesso controlado |
| Credenciais de integração | tokens/segredos | Guardados em Vault/SecretsManager, nunca em texto plano |
| IP/endpoints | IP de login/ações | Usar para segurança; não compartilhar externamente |

- Consentimento/legítimo interesse B2B: registrar timestamp e base legal no onboarding.  
- DSAR: endpoint para exportar/apagar dados do usuário (soft delete + anonimização).  
- Acesso por papel (RBAC) e tenant scoping obrigatório.

---

## 6) Auditoria e rastreabilidade

- `audit_logs` é append-only; usar tabela particionada por mês.  
- Campos mínimos: `id, timestamp, tenant_id, user_id (nullable), action, entity_type, entity_id, input, output, confidence, ip_address`.  
- Logs de modelos (prompt/response) devem ser vinculados a `entity_id` e `tenant_id`, com mask de PII (e.g., substituir e-mails).  
- Trilha de configuração: mudanças em `configs` geram evento `config.changed`.

---

## 7) Eventos (pub/sub interno)

| Evento | Payload mínimo | Consumidores |
|--------|----------------|--------------|
| `cobranca.approved` | cobranca_id, tenant_id, approved_by | Worker → envio |
| `cobranca.sent` | cobranca_id, channel | Observabilidade |
| `conciliacao.completed` | conciliacao_id, divergencias | Dashboard, alertas |
| `pagamento.approved` | pagamento_id | ERP connector |
| `hil.pending` | entity_type, entity_id | Notificação/UI |
| `hil.resolved` | entity_type, entity_id, outcome | Dashboard |
| `config.changed` | tenant_id, diff | Auditoria |

---

## 8) Decisões
- **Decidido**: Multi-tenant por `tenant_id` (row-level) com índices por tenant.
- **Decidido**: Audit log append-only com retenção de 5 anos.
- **Decidido**: Retenção de arquivos de boleto/extrato por 180 dias.
- **[OPEN]**: Retenção de dados operacionais (24 meses) — validar com jurídico/ICP.
- **[OPEN]**: Coleção vetorial para ledger (conciliacao) — validar necessidade no MVP.

## Riscos
- R-003: Segurança/LGPD — minimizar PII, mask em logs, isolamento por tenant.
- R-005: Dados/integrações imprevisíveis — schema e validação de ingestão.
- R-012: Custo — retenção e limpeza periódica para conter storage/LLM.

## Próximos passos
1) Validar retenção com jurídico/ICP.  
2) Implementar migrations (Alembic) com constraints e índices listados.  
3) Implementar purge jobs (storage + vetores) e mascaramento em logs.  


