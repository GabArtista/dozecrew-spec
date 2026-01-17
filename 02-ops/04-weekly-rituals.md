---
title: Rituais Semanais e Métricas (Company OS)
status: draft
owners:
  - Gabriel
  - Miguel
updated: 2026-01-16
links:
  - /docs/02-ops/01-operating-model.md
  - /docs/02-ops/02-intake-process.md
  - /docs/02-ops/03-delivery-process.md
  - /docs/02-ops/05-templates/TPL-005-weekly-metrics-snapshot.md
  - /docs/00-index/decision-log.md
tags:
  - ops
  - rituals
  - metrics
  - ia-first
---

## Contexto
Com 2 fundadores, “rituais” só valem se produzirem decisões, foco e aprendizado rápido. O resto vira overhead (R-009).

## Objetivo
Definir rotina semanal (rituais), agendas e métricas para manter foco, qualidade e previsibilidade.

## Escopo
- Rotina semanal (reuniões e cadência).
- Métricas por área e um snapshot semanal.
- Regras de tomada de decisão e WIP.

## Não-escopo
- Gestão de equipe grande e políticas de performance.

## Rotina semanal (rituais)

### Segunda — Planejamento (45 min)
- **Entrada**: métricas da semana anterior (TPL-005), status de pilotos, pipeline.
- **Saída**:
  - Top 3 prioridades da semana (com dono e prazo)
  - Limites de WIP (máx. 1 iniciativa externa “grande” em execução) [OPEN]
  - Riscos da semana e mitigação

### Terça/Quinta — Check-in de execução (15 min)
- **Formato**: async-first; reunião só se houver bloqueio.
- **Perguntas**:
  - O que foi entregue desde o último check-in?
  - Qual o próximo “milestone” (48h)?
  - Bloqueios (e quem resolve)?

### Quarta — Triage de Intake (30 min)
- **Entrada**: leads com formulário completo.
- **Saída**: scorecard + Go/No-Go/Maybe + próximos passos.

### Sexta — Review & Learning (60 min)
- **Entrada**: resultados de pilotos/experimentos, incidentes, métricas.
- **Saída**:
  - Decisões (o que continua / corta / muda)
  - 1 melhoria de processo (máx. 1 por semana)
  - 1 item de padronização (utilitário interno U1/U2/U3)

## Métricas (dashboard mínimo)

### Vendas
- resposta %, reuniões %, propostas %, pilotos pagos
- tempo 1º contato → piloto assinado

### Entrega
- lead time por etapa (Discovery/MVP/Piloto/Escala)
- incidentes/semana e tempo de correção
- custo por execução (infra/LLM) [OPEN]

### Produto
- hipóteses testadas/semana
- % trabalho reaproveitado (componentes) [OPEN]

### Finanças
- receita (setup + recorrência), margem estimada, runway [OPEN]

## Decisões
- **Decidido**: rituais com saídas obrigatórias (decisões e próximos passos).
- **[OPEN]**: ferramenta/fonte única do dashboard (planilha vs Notion vs Git).

## Riscos
- R-009 (overhead), R-010 (burnout).

## Próximos passos
- Adotar `TPL-005` na sexta-feira e usar como entrada do planejamento de segunda.
- Definir thresholds de alerta (ex.: incidentes > X, custo > Y) [OPEN].



