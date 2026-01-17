---
title: "Core Hub — LLMOps & Segurança"
status: draft
owners:
  - Gabriel
updated: 2026-01-16
links:
  - /docs/03-products/core-hub/01-prd.md
  - /docs/03-products/core-hub/02-spec.md
  - /docs/03-products/core-hub/03-architecture.md
  - /docs/03-products/core-hub/04-api.md
  - /docs/03-products/core-hub/05-data.md
  - /docs/03-products/core-hub/07-testing.md
  - /docs/00-index/decision-log.md
tags:
  - llmops
  - safety
  - governance
  - ia-first
---

## Contexto
Padrões de LLMOps, segurança e qualidade para os fluxos do Core Hub (cobrança, conciliação, contas a pagar).

## Objetivo
Garantir que uso de LLMs seja seguro, observável, economicamente viável e com qualidade controlada (HIL + guardrails).

## Escopo
- Seleção de modelos, fallback e caching.
- Prompts, guardrails, filtros.
- Observabilidade (latência, custo, qualidade).
- Avaliação automática e humana.
- Resposta a incidentes.

## Não-escopo
- Fine-tuning dedicado (avaliar v1.1+).
- Ferramentas de A/B infra-estruturadas (usar toggles simples no MVP).

---

## 1) Modelos e provedores

| Uso | Modelo primário | Fallback | Observações |
|-----|-----------------|----------|-------------|
| Geração de mensagens (cobrança) | GPT-4o mini | Claude Haiku | Custo x qualidade |
| Classificação / matching | GPT-4o mini | gpt-3.5-turbo | Pode substituir por modelos menores se accuracy ≥ threshold |
| Extração (OCR pós-parser) | Regras + GPT-4o mini | — | Evitar LLM se parser resolve |
| Embeddings | text-embedding-3-small | — | Custo baixo |

- Rate limit por tenant e por job; fila assíncrona.  
- Caching (chave: prompt hash + contexto + versão de template) para respostas repetitivas.

---

## 2) Prompts e templates

- Versionamento: `prompts/<fluxo>/<versao>.yaml`.  
- Cada prompt inclui: objetivo, instruções, formato de saída (JSON), limites (sem inventar dados), idioma (PT-BR).  
- Injetar contexto mínimo: dados da fatura/linha, políticas do cliente, limites.  
- Não expor PII desnecessária (substituir campos não usados).

---

## 3) Guardrails

| Controle | Implementação |
|----------|---------------|
| Output schema | Pydantic + validação; rejeitar/retentar se inválido |
| Confiança mínima | Se `< threshold`, exigir HIL; caso contrário, descartar saída |
| Ações sensíveis | `require_approval=true` por default (cobrança, pagamentos, ajustes) |
| Regex/keyword filters | Bloquear linguagem ofensiva ou menções a dados internos |
| Timeouts/retries | 2 retries com backoff; se falhar, marcar como `failed` e notificar |
| Rate limiting | Por tenant e por fluxo |

---

## 4) Observabilidade (LLM)

| Métrica | Descrição | Threshold inicial |
|---------|-----------|-------------------|
| Latência p95 | Tempo de resposta do modelo | ≤ 4s (geração); ≤ 2s (classificação) |
| Custo por execução | $ LLM por fluxo | ≤ R$0,50 por execução [OPEN] |
| Taxa de erro | % falhas/timeout | ≤ 2% |
| Qualidade (auto-eval) | Pontuação de rubric interna | ≥ 0,85 |
| Aderência a formato | % respostas válidas no schema | ≥ 98% |

- Tracing por request: prompt, tokens, custo, latência, modelo, versão do template.  
- Logs sensíveis com mask de PII (e-mails, CPFs).  
- Painel semanal: custo LLM por cliente, por fluxo; qualidade; incidentes.

---

## 5) Avaliação (offline e online)

### Offline (pré-deploy)
- Conjunto de exemplos anonimizados (por fluxo) com gabarito.
- Métricas: exatidão de campos, aderência a formato, hallucination rate.
- Gate: não promover modelo/template se score < 0,85.

### Online (pós-deploy)
- Amostragem de 5–10% das execuções para revisão humana.
- Feedback de HIL alimenta dataset (reinforcement via prompts, não RLHF).
- Regressão: rodar suite de casos críticos a cada mudança de prompt/modelo.

---

## 6) Segurança e abuso

| Risco | Mitigação |
|-------|-----------|
| Prompt injection | Sanitize entradas; delimitar contexto; checar instruções proibidas |
| Data leakage | Mask de PII, limites de contexto por tenant, sem dados de outros tenants |
| Uso malicioso (spam) | Rate limits, horário comercial, verificação de destinação |
| Ações erradas | HIL obrigatório; rollback; logs imutáveis |

---

## 7) Incidentes e rollback

| Cenário | Ação |
|---------|------|
| Saída errada em produção | Registrar incidente, desativar auto-aprovação, reroute para HIL |
| Custo fora do normal | Ativar cache agressivo, trocar para modelo mais barato, limitar volume |
| Latência alta | Fila priorizada, fallback para modelo mais rápido, reduzir contexto |
| Vazamento/PII | Kill switch do fluxo, rotate credenciais, notificar cliente, revisão jurídica |

Playbook: usar `TPL-006-incident-report.md` (já existente) e registrar no audit log.

---

## 8) Decisões
- **Decidido**: HIL por default e guardrails via validação de schema.
- **Decidido**: Caching + versionamento de prompts.
- **Decidido**: Métricas mínimas de latência, custo, qualidade.
- **[OPEN]**: Threshold final de custo por execução (R$0,50 é estimativa).
- **[OPEN]**: Ferramenta de observabilidade LLM (LangSmith vs custom).

## Riscos
- R-006: Qualidade → auto-eval + HIL + rollback.
- R-012: Custo → caching, modelos menores, limites.
- R-003: Segurança/LGPD → mask de PII, isolamento de tenant.

## Próximos passos
1) Criar dataset de avaliação com 20 casos por fluxo (anonimizados).  
2) Implementar tracing + métricas de custo/latência.  
3) Definir ferramenta de observabilidade LLM (LangSmith vs custom) [OPEN].  


