---
title: Processo de Intake (Entrada Universal de Projetos)
status: draft
owners:
  - Gabriel
  - Miguel
updated: 2026-01-16
links:
  - /docs/00-index/decision-log.md
  - /docs/01-company/01-thesis.md
  - /docs/01-company/03-portfolio.md
  - /docs/02-ops/05-templates/TPL-001-intake-form.md
  - /docs/02-ops/05-templates/TPL-002-triage-scorecard.md
tags:
  - ops
  - intake
  - prioritization
  - ia-first
---

## Contexto
Com 2 fundadores, o maior risco é aceitar iniciativas com escopo e integrações imprevisíveis ou canal instável. O Intake padroniza decisão, reduz retrabalho e cria rastreabilidade.

## Objetivo
Definir um processo universal para entrada de projetos/leads: formulário → triagem → score ICE + risco → decisão Go/No-Go → handoff para entrega.

## Escopo
- Formulário mínimo (dados para decisão).
- Triagem e score (ICE + risco de canal + risco de entrega).
- Regras de decisão e registro.

## Não-escopo
- CRM completo e automações de prospecção (apenas o processo de decisão).

## Formulário (entrada)
Usar `TPL-001-intake-form.md`.

Campos obrigatórios:
- Problema e contexto (o que dói, onde dói, frequência).
- “Job to be done” + resultado esperado (métrica).
- Volume (por dia/semana/mês) e impacto (tempo, erro, dinheiro).
- Sistemas envolvidos (até 2 desejável no piloto).
- Dados disponíveis e acesso (restrições LGPD/compliance).
- Prazo e urgência (por quê agora).
- Orçamento e sponsor (quem decide e paga).

## Triagem (reunião de 30 min)
Cadência: 2x/semana (ou sob demanda).

Entrada:
- Formulário completo (sem isso, **não triageia**).

Saída:
- Scorecard preenchido (`TPL-002`) + decisão preliminar.

## Score (ICE + risco)
Usar `TPL-002-triage-scorecard.md`.

### 1) ICE (Impacto, Confiança, Esforço)
Escala: 1 (baixo) a 5 (alto).
- **Impacto (I)**: potencial de valor (R$/horas/erro evitado), tamanho do mercado e repetibilidade.
- **Confiança (C)**: evidência (conversas, dados, LOI/piloto pago, clareza do problema).
- **Esforço (E)**: complexidade total (integrações, dados, UX, risco de exceções).

Score base:
- **ICE = (I × C) / E**

### 2) Risco de canal (RC)
Escala: 1 (baixo) a 5 (alto).
Pergunta: “Para vender isso, dependemos de ads/SEO/plataformas instáveis no curto prazo?”
- 1–2: outbound/parcerias controláveis
- 3: misto
- 4–5: forte dependência de ads/SEO/plataformas

### 3) Risco de entrega (RE)
Escala: 1 (baixo) a 5 (alto).
Pergunta: “O piloto exige mais de 2 integrações, dados ruins ou ações sensíveis sem guardrails?”

Score final (para ordenar backlog de oportunidades):
- **Score Final = ICE × (1 / (1 + 0.25×RC + 0.35×RE))**

[OPEN] Ajustar pesos após 2 semanas com dados reais.

## Decisão Go/No-Go (regras)
### Go (piloto)
Condições mínimas:
- Sponsor e orçamento (piloto pago ou LOI com valor/prazo).
- Resultado mensurável definido.
- ≤ 2 integrações no piloto (ou justificativa escrita).
- Risco de dados/compliance mitigável com guardrails.

### No-Go (recusar ou adiar)
Motivos típicos:
- Sem dono (ninguém decide/paga).
- Escopo aberto (“automatiza tudo”).
- Integrações/dados inviáveis no prazo do piloto.
- Canal depende de ads/SEO/plataformas para ser viável agora.

### Maybe (incubação)
- Transformar em hipótese/experimento de 7–14 dias, sem compromisso de entrega.

## Registro e handoff
- Decisão e rationale: registrar no Decision Log quando for:
  - mudança de tese/portfólio, ou
  - aceitação de exceção (ex.: 3 integrações).
- Handoff para Delivery:
  - anexar scorecard + SOW (template) + checklist de prontidão.

## Decisões
- **Decidido**: Intake obrigatório via formulário + triagem + score ICE+risco.
- **[OPEN]**: thresholds numéricos para “Go automático” vs “precisa discussão”.

## Riscos
- R-001 (escopo), R-004 (canal), R-005 (integrações), R-011 (handoff).

## Próximos passos
- Rodar o Intake em 10 leads e calibrar pesos/thresholds.
- Criar taxonomia de motivos de No-Go e perdas (para aprendizado).



