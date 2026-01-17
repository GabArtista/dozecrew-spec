---
title: GTM (Go-to-Market) — v1 (Outbond + Parcerias)
status: draft
owners:
  - Miguel
  - Gabriel
updated: 2026-01-16
links:
  - /docs/01-company/01-thesis.md
  - /docs/01-company/03-portfolio.md
  - /docs/01-company/04-pricing.md
  - /docs/02-ops/02-intake-process.md
  - /docs/05-research/experiments-14d/EXP-001-outbound.md
  - /docs/00-index/decision-log.md
  - /docs/01-company/06-risk-register.md
tags:
  - company
  - gtm
  - outbound
  - partnerships
  - ia-first
---

## Contexto
Portfólio inicial:
- **A1 (core)**: Copiloto de Rotinas Financeiras (backoffice) — wedge
- **B1 (alternativa)**: Conhecimento Vivo + QA (suporte/vendas)

Restrição: 2 fundadores → canal inicial precisa ser controlável e de baixo risco (evitar ads/SEO no começo).

## Objetivo
Definir GTM v1 executável (mensagens, canais, cadência e métricas) para validar ICP/wedge/preço e fechar 1–2 pilotos pagos.

## Escopo
- ICPs iniciais (A1 e B1) + hipóteses.
- Mensagens (value prop, prova, CTA).
- Canais (outbound e parcerias) + cadência.
- Métricas e thresholds.

## Não-escopo
- Estratégia completa de conteúdo/SEO.
- Growth/ads e funis automatizados complexos.

## ICPs e wedges (v1)

### A1 (core) — ICP inicial
[ASSUMPTION] Brasil, venda B2B via outbound + parcerias.
- **ICP-A1.1**: BPO financeiro / escritório contábil com volume e SLA (10–50 clientes ativos).
- **ICP-A1.2**: PME 20–200 com financeiro internalizado e alto volume (boletos/cobrança/conciliação).

**Wedge A1 (candidato)**: “Cobrança + conciliação” OU “Contas a pagar com validação” [OPEN].

**Oferta**: piloto 14–30 dias com 1 fluxo fim-a-fim, ≤2 integrações, human-in-the-loop e trilha auditável.

### B1 (alternativa) — ICP inicial
- **ICP-B1.1**: SaaS B2B com suporte em PT-BR (Head de CS/Support), documentação complexa.
- **ICP-B1.2**: E-commerce com alto volume no WhatsApp (supervisão de atendimento) [OPEN].

**Wedge B1 (candidato)**: “Respostas citadas + painel de aprovação” com relatório semanal de qualidade/ROI.

## Proposta e mensagem (v1)

### Mensagem A1 (backoffice)
- **Dor**: tempo + erro + retrabalho em rotinas repetitivas; falta de trilha e previsibilidade.
- **Promessa**: “reduzir horas/semana e erros em 30 dias, sem trocar seus sistemas”.
- **Prova**: human-in-the-loop + logs auditáveis + métrica antes/depois.
- **CTA**: “15 min para mapear 1 rotina e dizer se dá ROI em 14 dias?”

### Mensagem B1 (suporte)
- **Dor**: respostas inconsistentes, base desatualizada, TMA alto.
- **Promessa**: “respostas consistentes e citadas + governança”.
- **Prova**: painel de aprovação + avaliação contínua + relatório.
- **CTA**: “15 min para avaliar sua base e estimar deflexão/TMA em 14 dias?”

## Canais e cadência

### Canal 1 — Outbound (primário)
- Sequência: e-mail + LinkedIn + (WhatsApp só com contexto/permite) [OPEN].
- Cadência operacional em `/docs/05-research/experiments-14d/EXP-001-outbound.md`.

### Canal 2 — Parcerias (secundário, mas escalável)
- **A1**: parcerias com contabilidades/BPOs e ERPs locais (quando fizer sentido) [OPEN].
- **B1**: parcerias com consultorias de CS, agências e integradores de Zendesk/Intercom [OPEN].

**Oferta para parceiro**:
- indicação com % de recorrência por X meses [OPEN] OU fee fixo por piloto fechado.

## Métricas e thresholds (para decisão)
Objetivo macro: escolher foco (A1 vs B1) com sinais pagantes.

### Métricas de canal (por tese/oferta)
- Resposta outbound ≥ 8%
- Reuniões ≥ 3% dos contatos
- Propostas enviadas ≥ 30% das reuniões

### Métricas de compra (WTP)
- ≥ 2 pilotos pagos OU LOIs com valor e prazo por oferta em 14 dias.

### Métricas de entrega (viabilidade)
- “Primeiro valor” ≤ 14 dias
- ≤ 2 integrações no piloto (exceções registradas)

## IA-First na operação de GTM
- Geração assistida de listas (enriquecimento) com revisão humana.
- Personalização de 1 linha por lead (baseada em sinal público) com guardrails (sem inventar).
- Classificação automática de respostas (interessado/objecção/fora do ICP) com revisão humana.

## Decisões
- **Decidido**: outbound + parcerias como GTM inicial.
- **[OPEN]**: wedge A1 definitivo (cobrança vs conciliação vs AP).
- **[OPEN]**: canal prioritário para B1 (WhatsApp vs Zendesk/Intercom).
- **[OPEN]**: política de parceria (% vs fee).

## Riscos
- R-014 (spam/entregabilidade), R-015 (ICP errado), R-016 (compliance), R-004 (canal).

## Próximos passos
- Rodar EXP-001 por 48h e ajustar ICP/mensagem com base em respostas e objeções.
- Escolher 1 wedge A1 para piloto (com base em 5 conversas) e atualizar Decision Log.



