---
title: TPL-002 — Triage Scorecard (ICE + Risco)
status: active
owners:
  - Miguel
  - Gabriel
updated: 2026-01-16
links:
  - /docs/02-ops/02-intake-process.md
  - /docs/00-index/decision-log.md
tags:
  - template
  - ops
  - prioritization
---

## Contexto
Scorecard para decidir Go/No-Go e ordenar oportunidades com base em impacto e risco.

## Objetivo
Converter informações do Intake em uma decisão rastreável e comparável.

## Escopo
Aplicar a qualquer lead/projeto/ideia.

## Não-escopo
Forecast financeiro detalhado.

## Dados do caso
- Nome do caso:
- Oferta candidata: A1 / B1 / C1 / Outro [OPEN]
- Fonte: outbound / parceria / inbound / outro
- Sponsor existe? (sim/não)
- Orçamento/LOI? (sim/não)

## ICE
Escala 1–5.
- **Impacto (I)**:
  - Nota:
  - Evidência (por quê):
- **Confiança (C)**:
  - Nota:
  - Evidência (por quê):
- **Esforço (E)**:
  - Nota:
  - Evidência (por quê):

ICE = (I × C) / E

## Riscos
Escala 1–5.
- **Risco de canal (RC)**:
  - Nota:
  - Por quê:
- **Risco de entrega (RE)**:
  - Nota:
  - Por quê:

Score Final = ICE × (1 / (1 + 0.25×RC + 0.35×RE))

## Decisão
- Go / No-Go / Maybe:
- Condições (se Go):
  - Escopo fechado do piloto:
  - Integrações (≤2):
  - Métrica-alvo:
- Se exceção (ex.: 3 integrações), registrar decisão no Decision Log? (sim/não)

## Riscos (resumo)
- Principais riscos:
- Mitigação proposta:

## Próximos passos
- Próxima ação:
- Dono:
- Prazo:



