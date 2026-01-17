---
title: EXP-001 — Outbound (14 dias) para validar ICP/Wedge/Preço
status: draft
owners:
  - Miguel
  - Gabriel
updated: 2026-01-16
links:
  - /docs/01-company/05-gtm.md
  - /docs/01-company/03-portfolio.md
  - /docs/01-company/04-pricing.md
  - /docs/02-ops/02-intake-process.md
  - /docs/00-index/decision-log.md
  - /docs/01-company/06-risk-register.md
tags:
  - research
  - experiment
  - outbound
  - gtm
---

## Contexto
Este experimento operacionaliza o critério de 14 dias: testar canal, dor/orçamento (WTP) e viabilidade de entrega (≤2 integrações) antes de construir pesado.

## Objetivo
Em 14 dias, gerar evidência para escolher foco (A1 vs B1) e fechar 1–2 pilotos pagos (ou LOIs) com escopo fechado.

## Escopo
- Outbound com cadência diária.
- 2 mensagens (A1 e B1) e no máximo 2 variações por vez.
- Tracking e métricas/thresholds.

## Não-escopo
- Ads e SEO.
- Automatizações agressivas sem revisão humana.

## Hipóteses
- **H1 (canal)**: outbound segmentado gera resposta ≥ 8% e reuniões ≥ 3%.
- **H2 (WTP)**: há disposição a pagar por piloto (setup + mensalidade) com limites explícitos.
- **H3 (viabilidade)**: conseguimos desenhar piloto com ≤ 2 integrações e primeiro valor ≤ 14 dias.

## [ASSUMPTION] ICP/Wedge/Preço (v1)
Se não estiver explícito na conversa, usar:
- **A1 ICP**: BPO financeiro/contabilidade com volume e SLA.
- **A1 Wedge**: cobrança OU conciliação (escolher 1 ao final de 48h).
- **A1 preço**: setup R$ 5k–20k; mensalidade R$ 2k–10k.
- **B1 ICP**: SaaS B2B com CS/Support > 5.
- **B1 wedge**: respostas citadas + painel de aprovação + relatório semanal.
- **B1 preço**: setup R$ 1k–8k; mensalidade R$ 1k–6k.

## Setup (Dia 0)
### Lista e segmentação
- Montar 2 listas separadas (A1 e B1): 80–120 contatos cada.
- Campos mínimos por lead:
  - nome, cargo, empresa, segmento, tamanho, região [OPEN]
  - “sinal” para personalização (1 linha) (ex.: vaga, post, página “financeiro”, “suporte”) [OPEN]

### Tracking (planilha/CRM simples) — campos
- Lead ID, oferta (A1/B1), segmento, canal (email/LI/WA)
- Mensagem v1/v2, data D1/D2/D3...
- Status: enviado / respondeu / reunião / proposta / piloto / perdido
- Motivo de resposta: interessado / sem dor / sem prioridade / sem budget / já tem / compliance / outro
- Próxima ação e data

## Cadência (14 dias) — rotina diária
Meta: consistência > volume.

### Dia 1–2 (48h): calibragem rápida
- Enviar 20–30 mensagens por oferta/dia.
- Medir:
  - respostas, objeções, termos usados pelos ICPs, CTA
- Ajustar em 48h:
  - se resposta < 5%: trocar segmento ou promessa antes de “mexer no produto”.

### Dias 3–10: execução
- Enviar 30–50 mensagens/dia total (somando ofertas), mantendo qualidade.
- Agendar 3–6 reuniões/semana (alvo).
- Fazer triagem via Intake (form + scorecard) para oportunidades reais.

### Dias 11–14: fechamento
- Converter reuniões em:
  - 2 propostas (TPL-003) por oferta [alvo]
  - 1–2 pilotos pagos totais
- Consolidar aprendizados e registrar decisão (foco) no Decision Log.

## Scripts (prontos para uso)
Regras:
- 1 linha personalizada baseada em sinal real (sem inventar).
- CTA de 15 min.
- Sempre oferecer opt-out.

### Script A1 — e-mail #1
Assunto: {Empresa} — reduzir retrabalho no financeiro em 30 dias?

Olá {Nome}, vi {sinal_real}.  
Trabalhamos com automação “IA-first” para rotinas de backoffice com **trilha auditável** e **aprovação humana** quando necessário.

Em geral, em 14–30 dias dá para atacar 1 rotina (ex.: cobrança/conciliação) e medir horas poupadas + erros evitados, sem trocar seus sistemas.

Faz sentido um papo de 15 min para mapear 1 rotina e eu dizer se dá ROI em ≤14 dias?  
Se não for prioridade agora, posso encerrar por aqui (só me avisar).

### Script A1 — follow-up #1 (D+2)
Oi {Nome}, só confirmando se vale explorar.  
Pergunta direta: hoje o gargalo maior é **cobrança**, **conciliação** ou **contas a pagar**?

### Script B1 — LinkedIn DM #1
Oi {Nome}, vi {sinal_real}.  
Estamos montando um piloto de 14–30 dias para suporte: **respostas citadas + painel de aprovação** + relatório semanal (deflexão/TMA/CSAT).

Se eu olhar sua base/FAQ por alto, você toparia 15 min para estimarmos o ganho e dizer se vale piloto?

### Script WhatsApp (apenas com contexto) [OPEN]
[OPEN] Usar WhatsApp somente se houver relação/contexto (indicação, evento, resposta prévia) e opt-out explícito.

## Métricas e thresholds (pass/fail)
Avaliar por oferta (A1 e B1).

### Canal
- Resposta ≥ 8%
- Reuniões ≥ 3%

### WTP
- ≥ 2 pilotos pagos OU LOIs com valor e prazo (em 14 dias)

### Viabilidade
- ≤ 2 integrações no piloto
- “Primeiro valor” ≤ 14 dias

## Decisões
- **Decidido**: ajustar ICP/mensagem em 48h se resposta < 5%.
- **[OPEN]**: wedge A1 final (cobrança vs conciliação vs AP) após 48h de sinais.
- **[OPEN]**: canal WhatsApp (permitido/banido) conforme compliance e resposta.

## Riscos
- R-014 (spam/entregabilidade), R-015 (ICP errado), R-016 (compliance).

## Próximos passos
- Executar Dia 1–2 e registrar:
  - top 3 objeções
  - top 3 frases que mais funcionaram
  - decisão de wedge A1 (ou troca de segmento)
- No Dia 14: registrar decisão final (A1 vs B1) no Decision Log com evidências.



