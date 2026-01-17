---
title: Processo de Entrega (Discovery → MVP → Piloto → Escala)
status: draft
owners:
  - Gabriel
  - Miguel
updated: 2026-01-16
links:
  - /docs/00-index/decision-log.md
  - /docs/01-company/03-portfolio.md
  - /docs/02-ops/02-intake-process.md
  - /docs/02-ops/05-templates/TPL-003-pilot-sow.md
  - /docs/02-ops/05-templates/TPL-006-incident-report.md
tags:
  - ops
  - delivery
  - quality
  - ia-first
---

## Contexto
O diferencial IA-First depende de entregar rápido sem sacrificar qualidade/segurança. O processo abaixo reduz risco de “agent fazendo besteira” e de integrações imprevisíveis, mantendo escopo fechado.

## Objetivo
Padronizar execução em 4 etapas com checklists e Definition-of-Done (DoD), garantindo observabilidade, guardrails e evidência de valor.

## Escopo
- Workflow: Discovery → MVP → Piloto → Escala.
- Checklists e DoD por etapa.
- Política de mudanças de escopo e incidentes.

## Não-escopo
- Arquitetura técnica detalhada e padrões de código (ficam no SpecKit) [OPEN].

## Etapa 1 — Discovery (1–3 dias)
### Objetivo
Definir problema, métrica, limites, dados e risco antes de construir.

### Checklist
- Confirmar “job to be done” e métrica de valor (ex.: horas poupadas/semana).
- Mapear processo atual (passos, exceções, sistemas).
- Definir wedge: 1 fluxo fim-a-fim (não “automatizar tudo”).
- Identificar dados/fonte e permissão (LGPD/compliance).
- Definir guardrails (o que exige aprovação humana).

### DoD (Definition-of-Done)
- Métrica-alvo definida e mensurável.
- Escopo do piloto fechado e assinado (SOW).
- Checklist de prontidão concluído (dados + integrações).

## Etapa 2 — MVP (3–7 dias)
### Objetivo
Construir o mínimo que gera valor com segurança (human-in-the-loop).

### Checklist
- Pipeline mínimo de dados/integr. (≤ 2 sistemas).
- RAG/agent com:
  - fontes explícitas/citações (quando aplicável)
  - níveis de confiança [OPEN]
  - aprovações para ações sensíveis
- Observabilidade:
  - logs e trilha auditável
  - métricas de custo/latência [OPEN]
- Testes de casos críticos (10–20 casos reais/anônimos) [OPEN].

### DoD
- Fluxo completo funciona em staging.
- Guardrails ativos (aprovação humana onde necessário).
- Métricas instrumentadas (mesmo que simples).

## Etapa 3 — Piloto (7–21 dias)
### Objetivo
Rodar com usuários reais e gerar prova (resultado + confiabilidade).

### Checklist
- Kickoff com cliente: objetivos, limites, rotina de check-in.
- Operação:
  - SLA interno de suporte
  - coleta de feedback estruturada
- Medição semanal:
  - valor (horas/erros/deflexão etc.)
  - qualidade (taxa de aprovação humana, incidentes)
- Mudança de escopo:
  - toda mudança vira item com ICE+risco e ajuste de preço/prazo.

### DoD
- Relatório de resultados do piloto (antes/depois).
- Lista de gaps (produto/integrações) priorizada.
- Decisão: Escala vs Encerrar vs Re-piloto.

## Etapa 4 — Escala (4–12 semanas)
### Objetivo
Tornar repetível, reduzir custo unitário e aumentar confiabilidade.

### Checklist
- Padronizar o que foi “sob medida” em componentes (U1–U3).
- Segurança/compliance:
  - política de retenção, revisão de acessos, auditoria
- Operação:
  - runbook + treinamento
  - monitoramento e alertas

### DoD
- SLOs definidos e medidos.
- Processo replicável para 2º cliente do mesmo wedge.

## Gestão de mudanças e incidentes
- **Mudança de escopo**: documentar, reestimar, ajustar contrato.
- **Incidente**: registrar em `TPL-006` e criar ação corretiva (produto/processo).

## Decisões
- **Decidido**: human-in-the-loop e trilha auditável como padrão para ações sensíveis.
- **[OPEN]**: definição formal de níveis de confiança e SLOs iniciais.

## Riscos
- R-006 (qualidade), R-005 (integrações), R-003 (dados/compliance).

## Próximos passos
- Criar checklist de “prontidão de dados” detalhado no SpecKit [OPEN].
- Definir conjunto mínimo de testes e métricas por oferta (A1 e B1).



