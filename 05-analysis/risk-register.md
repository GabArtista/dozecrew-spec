---
title: Risk Register
status: active
owners:
  - Gabriel
  - Miguel
updated: 2026-01-16
links:
  - /docs/00-index/decision-log.md
  - /docs/01-company/01-thesis.md
tags:
  - risk
  - governance
  - strategy
---

## Contexto
Registro de riscos estratégicos e operacionais da empresa “IA-First”, com mitigação e responsáveis.

## Objetivo
Evitar surpresas previsíveis, tornar trade-offs explícitos e orientar priorização (ICE + risco de canal).

## Escopo
- Riscos de mercado, canal, execução, tecnologia, segurança, jurídico e operação.

## Não-escopo
- Bugs pontuais sem impacto sistêmico.

## Riscos

### R-001 — Virar consultoria infinita (escopo sob medida) na Tese A
- **Probabilidade**: Alta
- **Impacto**: Alto
- **Mitigação**:
  - Definir **wedge fechado** (1–2 rotinas com ROI) e recusar demandas fora do pacote no piloto.
  - Catálogo de integrações suportadas + “limite de exceções”.
  - Preço com setup + mensalidade e cláusula de mudança de escopo.
- **Owner**: Miguel
- **Status**: Open
- **Sinais/Triggers**:
  - Clientes pedem 5+ rotinas no primeiro mês.
  - Cada projeto exige integrações totalmente novas.

### R-002 — Commoditização/concorrência alta na Tese B (RAG para suporte)
- **Probabilidade**: Alta
- **Impacto**: Médio/Alto
- **Mitigação**:
  - Diferenciar por **governança e qualidade**: citações, auditoria, guardrails, avaliação contínua.
  - Foco em canais BR (WhatsApp) e métricas de negócio (deflexão, CSAT, TMA).
  - Nichar ICP (ex.: SaaS B2B com documentação complexa).
- **Owner**: Miguel
- **Status**: Open
- **Sinais/Triggers**:
  - Objeção recorrente: “já temos chatbot/Intercom Fin/feature X”.
  - Pressão por preço com comparação direta a concorrentes.

### R-003 — Risco de segurança e privacidade de dados (clientes não liberam acesso)
- **Probabilidade**: Média
- **Impacto**: Alto
- **Mitigação**:
  - Oferecer opção **self-hosted**/[OPEN] ou isolamento por tenant.
  - Minimizar dados (least privilege), criptografia em trânsito/repouso e logs auditáveis.
  - Política de retenção + DPA/contratos padrão.
- **Owner**: Gabriel
- **Status**: Open
- **Sinais/Triggers**:
  - Rejeição por “LGPD/compliance” antes de piloto.
  - Exigência de SOC2/ISO logo no início (pode mudar ICP).

### R-004 — Canal inicial errado (dependência de ads/SEO/plataformas)
- **Probabilidade**: Média
- **Impacto**: Alto
- **Mitigação**:
  - Priorizar **outbound qualificado** + parcerias (BPO/contabilidade para A; integradores/CRMs para B).
  - Rodar experimentos de canal com thresholds (14 dias) antes de construir pesado.
- **Owner**: Miguel
- **Status**: Mitigating
- **Sinais/Triggers**:
  - CAC indireto (tempo) alto e baixa taxa de reuniões.
  - Leads só aparecem via canais “caros”/instáveis.

### R-005 — Integrações/ETL imprevisíveis (dados ruins, sistemas legados)
- **Probabilidade**: Alta
- **Impacto**: Alto
- **Mitigação**:
  - Checklist de “prontidão de dados” e versão mínima de integrações suportadas.
  - Construir conectores reutilizáveis e pipeline de validação (schemas + testes).
  - Human-in-the-loop para etapas frágeis no início.
- **Owner**: Gabriel
- **Status**: Open
- **Sinais/Triggers**:
  - 30%+ do esforço indo para limpeza manual recorrente.
  - Dependência de exportações manuais.

### R-006 — Falha de qualidade (alucinação/ações erradas) afetando confiança
- **Probabilidade**: Média
- **Impacto**: Alto
- **Mitigação**:
  - Guardrails: ações sensíveis sempre com aprovação; níveis de confiança.
  - Observabilidade (tracing, custos, avaliação) e rollback.
  - Testes de regressão com casos reais anonimizados.
- **Owner**: Gabriel
- **Status**: Open
- **Sinais/Triggers**:
  - Incidentes de resposta errada sem citação/explicação.
  - Necessidade de “desligar” o sistema por falta de confiança.

### R-007 — Dispersão de foco (portfólio amplo cedo demais)
- **Probabilidade**: Alta
- **Impacto**: Alto
- **Mitigação**:
  - Portfólio com **1 core (wedge)** + **1 alternativa**; o resto fica como “utilitário interno” até haver sinal de demanda.
  - Roadmap orientado por ICE + risco de canal; novas ofertas exigem decisão no Decision Log.
  - Limites de WIP (no máximo 1 iniciativa externa em execução por vez) [OPEN].
- **Owner**: Miguel
- **Status**: Open
- **Sinais/Triggers**:
  - 3+ ofertas sendo vendidas em paralelo sem métricas comparáveis.
  - Atrasos recorrentes por troca de contexto.

### R-008 — Precificação/embalagem erradas (valor claro, cobrança confusa)
- **Probabilidade**: Média
- **Impacto**: Alto
- **Mitigação**:
  - Proposta de piloto com escopo fechado + métricas de valor (horas, erros, SLA; deflexão, TMA, CSAT).
  - Usar setup + mensalidade com cláusula de mudança de escopo; evitar “por hora” no começo.
  - Coletar 10 ancoragens de preço (entrevistas) antes de fixar tabela [OPEN].
- **Owner**: Miguel
- **Status**: Open
- **Sinais/Triggers**:
  - Perda de deals por “não entendi o que estou comprando”.
  - Margem negativa por excesso de exceções.

### R-009 — Overhead de processo (rituais/processos viram “teatro”)
- **Probabilidade**: Média
- **Impacto**: Médio/Alto
- **Mitigação**:
  - Processos “mínimos viáveis”: templates curtos e métricas acionáveis.
  - Auditoria quinzenal: cortar etapas que não geram decisão/melhoria.
  - Timebox em rituais e decisões explícitas por reunião.
- **Owner**: Miguel
- **Status**: Open
- **Sinais/Triggers**:
  - Reuniões sem decisões ou sem próximos passos claros.
  - Tempo em rituais > 15% da semana por 2 semanas seguidas.

### R-010 — Burnout dos fundadores (capacidade limitada + múltiplas frentes)
- **Probabilidade**: Alta
- **Impacto**: Alto
- **Mitigação**:
  - Limites de WIP (1 iniciativa externa por vez) [OPEN] e agenda semanal protegida.
  - Automatizar rotinas internas (IA-First) e padronizar templates.
  - “Kill switch” de escopo: cortar features não essenciais ao piloto.
- **Owner**: Gabriel
- **Status**: Open
- **Sinais/Triggers**:
  - Atrasos recorrentes, noites/finais de semana constantes.
  - Aumento de bugs/incidentes e queda de qualidade.

### R-011 — Falhas de handoff (vendas ↔ entrega ↔ produto) em time pequeno
- **Probabilidade**: Média
- **Impacto**: Alto
- **Mitigação**:
  - Intake único + SOW de piloto + Definition-of-Done por etapa.
  - Um “DRI” (Directly Responsible Individual) por iniciativa.
  - Registro de decisões e mudanças de escopo em log.
- **Owner**: Miguel
- **Status**: Open
- **Sinais/Triggers**:
  - Cliente promete algo que não foi estimado/aceito.
  - Retrabalho por requisitos não documentados.

### R-012 — Unit economics invisíveis (custo LLM/infra explode com volume)
- **Probabilidade**: Média
- **Impacto**: Alto
- **Mitigação**:
  - Medir custo por execução/resposta desde o MVP (por cliente e por fluxo).
  - Limites contratuais (volume) e faixas de cobrança quando exceder [OPEN].
  - Caching, batch, modelos menores quando possível e guardrails para evitar loops.
- **Owner**: Gabriel
- **Status**: Open
- **Sinais/Triggers**:
  - Custo variável crescendo mais rápido que receita.
  - Latência e falhas em picos de volume.

### R-013 — Descontos e exceções corroem margem (precificação “flexível demais”)
- **Probabilidade**: Média
- **Impacto**: Médio/Alto
- **Mitigação**:
  - Política de desconto com critérios e aprovação (ex.: “troca por case/indicação”).
  - “Preço por exceção” (integração extra, volume extra) e não “dar de graça”.
  - Revisão mensal de margem por cliente [OPEN].
- **Owner**: Miguel
- **Status**: Open
- **Sinais/Triggers**:
  - Muitos deals fechando abaixo do piso.
  - Exceções viram padrão sem ajuste de preço.

### R-014 — Entregabilidade e reputação (outbound vira spam)
- **Probabilidade**: Média
- **Impacto**: Alto
- **Mitigação**:
  - Lista pequena e altamente segmentada; mensagens personalizadas por 1 linha.
  - Cadência com opt-out e respeito a canais (sem insistência).
  - Warm-up de domínio e higiene (SPF/DKIM/DMARC) [OPEN].
- **Owner**: Miguel
- **Status**: Open
- **Sinais/Triggers**:
  - Queda de resposta e aumento de bounces/spam reports.
  - Bloqueios em LinkedIn/WhatsApp.

### R-015 — ICP/wedge errado (mensagem não ressoa, baixa taxa de reunião)
- **Probabilidade**: Média
- **Impacto**: Alto
- **Mitigação**:
  - Ajuste em 48h: revisar ICP, promessa e wedge (trocar segmento antes de trocar produto).
  - Usar tracking por segmento e motivo de “não”.
  - Rodar A/B de 2 mensagens no máximo por vez.
- **Owner**: Miguel
- **Status**: Open
- **Sinais/Triggers**:
  - Reuniões < 3% e respostas < 8% após 80 contatos.
  - Objeção recorrente: “não é prioridade / não temos isso”.

### R-016 — Compliance (LGPD/consentimento em WhatsApp/e-mail)
- **Probabilidade**: Baixa/Média
- **Impacto**: Alto
- **Mitigação**:
  - Contato B2B com base em legítimo interesse, mensagem contextual e opt-out claro [OPEN: revisão jurídica].
  - Evitar dados sensíveis; manter logs do consentimento quando aplicável.
  - Preferir e-mail/LinkedIn no início; WhatsApp só com contexto e permissão.
- **Owner**: Gabriel
- **Status**: Open
- **Sinais/Triggers**:
  - Reclamações formais ou bloqueios por plataforma.
  - Cliente exige DPA/termos antes de qualquer troca.

### R-017 — Vazamento ou corrupção de dados (logs, arquivos, vetores)
- **Probabilidade**: Baixa/Média
- **Impacto**: Alto
- **Mitigação**:
  - Mask de PII em logs, segregação por `tenant_id`, criptografia em repouso.
  - Retenção limitada (180 dias para arquivos; 24 meses para dados operacionais [OPEN]).
  - Backups e testes de restore; auditoria de acessos a storage e vetores.
- **Owner**: Gabriel
- **Status**: Open
- **Sinais/Triggers**:
  - Acesso fora do horário/local esperado.
  - Crescimento anômalo de storage ou falhas de checksum.

### R-018 — Dependência/indisponibilidade de provedor de LLM
- **Probabilidade**: Média
- **Impacto**: Médio/Alto
- **Mitigação**:
  - Fallback de modelo/provedor (OpenAI ⇄ Anthropic), caching de respostas.
  - Rate limits internos e fila assíncrona para absorver picos.
  - Monitorar custo/latência por modelo e thresholds de troca.
- **Owner**: Gabriel
- **Status**: Open
- **Sinais/Triggers**:
  - Erros 5xx/latência alta do provedor.
  - Custo por execução acima do teto definido.

## Decisões
Ver `/docs/00-index/decision-log.md`.

## Próximos passos
- Completar a seção [OPEN] de segurança (self-hosted vs SaaS, baseline de compliance) após 3 entrevistas com ICP.
- Transformar mitigação em requisitos de produto (guardrails, auditoria, limites de escopo).


