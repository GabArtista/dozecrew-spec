---
title: "Core Hub — Release & Deploy Playbook"
status: draft
owners:
  - Miguel
  - Gabriel
updated: 2026-01-16
links:
  - /docs/03-products/core-hub/02-spec.md
  - /docs/03-products/core-hub/03-architecture.md
  - /docs/03-products/core-hub/04-api.md
  - /docs/03-products/core-hub/07-testing.md
  - /docs/00-index/decision-log.md
tags:
  - release
  - devops
  - core-hub
---

## Contexto
Plano de release/deploy para o Core Hub, cobrindo ambientes, versionamento, testes de smoke e rollback.

## Objetivo
Garantir releases pequenos, testados e reversíveis, com rastreabilidade.

## Escopo
- Branching, versionamento e tagging.
- Pipeline de CI/CD.
- Checklists de pré/pós-release.
- Rollback e feature flags.

## Não-escopo
- Infra detalhada (ver `03-architecture.md`).
- Gestão de incidentes (usar `TPL-006-incident-report.md`).

---

## 1) Branching e versionamento

- **Trunk-based** com `main`.  
- Feature branches curtas (`feat/*`, `fix/*`).  
- Merge via PR com revisão.  
- **SemVer**: `MAJOR.MINOR.PATCH`. MVP inicial = `0.1.0`.  
- Tag a cada release estável (`v0.1.0`, `v0.1.1`...).

---

## 2) Ambientes e promoção

| Ambiente | Uso | Gate |
|----------|-----|------|
| `local` | Dev | Sem gates |
| `staging` | QA / demo interna | Smoke + E2E chave |
| `production` | Cliente | Smoke + checklist + aprovação DRI |

Promoção: main → staging (auto) → production (manual approval).

---

## 3) Pipeline (CI/CD)

| Etapa | Checks |
|-------|--------|
| Test | Unit + integração + lint |
| Build | Imagens Docker (api, worker, frontend) |
| LLM Eval | Rodar suite curta offline (20 casos) |
| Deploy staging | Apply migrations, seed mínimo, smoke |
| Deploy prod | Smoke, migrações com flag, notificar |

---

## 4) Checklists

### Pré-release (staging)
- [ ] Tests/lint verdes.
- [ ] LLM eval ≥ thresholds.
- [ ] Migrations revisadas e idempotentes.
- [ ] Variáveis de ambiente e secrets setados.
- [ ] Feature flags default = seguro (HIL on).

### Pós-release (prod)
- [ ] Smoke: login, criar cobrança, aprovar, enviar (dry-run).
- [ ] Dashboard abre e mostra métricas.
- [ ] Logs sem erros críticos nos primeiros 30 min.
- [ ] Custo/latência LLM normal.

---

## 5) Rollout e rollback

- **Canary**: 1 instância com 10% do tráfego (quando em K8s).  
- **Feature flags**: desligar auto-aprovação, desligar novo fluxo.  
- **Rollback**: redeploy da última imagem + rollback de migração (se possível) ou hotfix.  
- Dados: migrations devem ter script de down sempre que seguro.

---

## 6) Migrações e dados

- Migrations via Alembic, com check de compatibilidade (expand → contract).  
- Nunca apagar coluna sem etapa de backfill/removal gradual.  
- Locks: evitar migrações que bloqueiem tabelas grandes; usar migrações em janelas controladas.  
- Backup antes de migrações destrutivas.

---

## 7) Comunicação

- Changelog em `CHANGELOG.md` (resumo por release).  
- Notificação interna (Slack/Email) após deploy com: versão, mudanças, riscos, rollbacks.  
- Para clientes: notificar apenas mudanças relevantes (se afetar fluxo/UX).

---

## 8) Decisões
- **Decidido**: Trunk-based + SemVer, tags por release.
- **Decidido**: LLM eval é gate para promoção.
- **[OPEN]**: Ferramenta de feature flags (LaunchDarkly vs open-source simples).

## Riscos
- R-006: Qualidade → gates de testes + LLM eval.
- R-012: Custo → monitorar antes/depois; rollback se custo explode.
- R-003: Segurança → secrets e migrações revisados; rollback rápido.

## Próximos passos
1) Configurar pipelines (GitHub Actions) com gates descritos.  
2) Adicionar smoke script automatizado (staging/prod).  
3) Definir ferramenta de feature flags [OPEN].  


