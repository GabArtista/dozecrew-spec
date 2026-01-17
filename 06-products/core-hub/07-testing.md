---
title: "Core Hub — Estratégia de Testes"
status: draft
owners:
  - Gabriel
updated: 2026-01-16
links:
  - /docs/03-products/core-hub/02-spec.md
  - /docs/03-products/core-hub/03-architecture.md
  - /docs/03-products/core-hub/04-api.md
  - /docs/03-products/core-hub/05-data.md
  - /docs/03-products/core-hub/06-llmops.md
  - /docs/00-index/decision-log.md
tags:
  - testing
  - quality
  - core-hub
---

## Contexto
Plano de testes para o Core Hub, garantindo qualidade funcional, segurança e custo controlado em fluxos IA-First.

## Objetivo
Definir pirâmide de testes, cenários críticos por fluxo (cobrança, conciliação, contas a pagar), critérios de aceite e automação mínima.

## Escopo
- Testes unitários, integração, contrato (API), e2e e LLM eval.
- Smoke/regressão em cada release.
- Casos de segurança, LGPD e abuso.

## Não-escopo
- Testes de performance extremos (carga massiva > v1).
- Testes de usabilidade formal (heurística apenas).

---

## 1) Pirâmide de testes (meta)

| Nível | Cobertura meta | Observações |
|-------|----------------|-------------|
| Unit | ≥ 70% dos módulos críticos | Validação de regras (RN-*) |
| Integração | Casos happy + erro para conectores | Mock de ERPs/bancos/e-mail |
| Contrato (API) | 100% endpoints críticos | Schemathesis/Prism/OpenAPI |
| E2E | 3–5 cenários chave por fluxo | Cypress/Playwright |
| LLM Eval | 20 casos por fluxo | Auto-eval + human spot-check |

---

## 2) Casos por fluxo (MVP)

### Cobrança
- Gera cobrança com fatura vencida + mensagem correta.
- Não duplica cobrança em 48h para mesmo cliente.
- Requer aprovação → só envia após HIL.
- Escala após `no_response` em 7 dias.
- Relatório semanal retorna métricas corretas.

### Conciliação
- Importa OFX/CSV válido; rejeita formato inválido.
- Match automático (valor+data) e por confiança ≥ 0.85.
- Divergência ≥ threshold exige HIL.
- Aplicar ajuste cria log e atualiza status.

### Contas a pagar
- OCR extrai campos obrigatórios do boleto.
- Detecta duplicidade por código de barras.
- Sugestão de classificação retorna conta + confiança.
- Pagamento só registra após aprovação.

---

## 3) Segurança / LGPD / abuso

- Auth: bloqueio após 5 tentativas, refresh token inválido é rejeitado.
- RBAC: `viewer` não aprova; `operator` não altera config; `admin` consegue.
- Rate limiting: 429 após exceder limite.
- PII em logs é mascarada.
- Upload de arquivo malicioso é bloqueado (tipo/size).
- Webhook/API key não aceita sem assinatura (quando houver).

---

## 4) LLM Eval

| Fluxo | Métrica | Threshold |
|-------|---------|-----------|
| Cobrança (mensagem) | Formato válido | ≥ 98% |
| Cobrança (mensagem) | Adequação (rubric) | ≥ 0.85 |
| Conciliação (sugestão) | Precisão de match | ≥ 0.85 |
| AP (classificação) | Acurácia de classe | ≥ 0.80 |

- Dataset: 20 exemplos anonimizados por fluxo.  
- Auto-eval + revisão humana de 10% das saídas em produção.

---

## 5) Automação e ferramentas

- Tests: `pytest`, `pytest-asyncio`, `responses/httpx` para mocks.
- Contract: OpenAPI + Schemathesis; snapshots para respostas.
- E2E: Playwright/Cypress (login, approvals, relatório).
- LLM eval: scripts Python + prompt versioning; armazenar métricas.

---

## 6) Critérios de aceite (MVP release)

- Todos os fluxos P0 cobertos por testes unit + integração + 3 E2E.
- LLM eval ≥ thresholds definidos.
- Sem P1/P0 bugs abertos no board.
- Smoke de deploy verde (staging → prod).

---

## 7) Smoke/regressão

| Momento | Conjunto mínimo |
|---------|-----------------|
| Pré-deploy | Login, criar cobrança, aprovar, enviar, ver dashboard |
| Pós-deploy (prod) | GET `/health`, listar approvals, criar cobrança em modo dry-run |

---

## 8) Decisões
- **Decidido**: Cobrir fluxos P0 com testes unit+integração+E2E.
- **Decidido**: LLM eval obrigatório antes de promover prompt/modelo.
- **[OPEN]**: Ferramenta de E2E (Cypress vs Playwright).

## Riscos
- R-006: Qualidade → LLM eval + HIL.
- R-012: Custo → evitar chamadas LLM em testes; usar fixtures.
- R-003: Segurança → testes de RBAC/rate limit obrigatórios.

## Próximos passos
1) Gerar suite inicial de dados de teste (anonimizados).  
2) Implementar contract tests a partir do OpenAPI.  
3) Escolher ferramenta E2E (Cypress/Playwright) [OPEN].  


