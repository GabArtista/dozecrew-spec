---
title: Decision Log
status: active
owners:
  - Gabriel
  - Miguel
updated: 2026-01-16
links:
  - /docs/01-company/01-thesis.md
  - /docs/01-company/02-positioning.md
  - /docs/01-company/06-risk-register.md
  - /docs/03-products/core-hub/01-prd.md
  - /docs/03-products/core-hub/02-spec.md
  - /docs/03-products/core-hub/03-architecture.md
  - /docs/03-products/core-hub/04-api.md
  - /docs/03-products/core-hub/05-data.md
  - /docs/03-products/core-hub/06-llmops.md
  - /docs/03-products/core-hub/07-testing.md
  - /docs/03-products/core-hub/08-release.md
  - /docs/06-backlog/mvp-sprints.md
  - /docs/00-index/glossary.md
  - /docs/04-portal/01-sitemap.md
  - /docs/04-portal/02-copy.md
  - /docs/04-portal/03-design-notes.md
  - /docs/04-portal/04-tracking.md
  - /docs/04-portal/05-contact-ops.md
  - /docs/04-portal/01-sitemap.md
  - /docs/04-portal/02-copy.md
  - /docs/04-portal/04-tracking.md
tags:
  - governance
  - decisions
  - strategy
---

## Contexto
Este documento registra decisões relevantes do projeto (empresa, operação e produto), com alternativas consideradas, racional e implicações.

## Objetivo
Manter um histórico auditável para evitar “redecidir” sem dados e garantir alinhamento entre estratégia, execução e riscos.

## Escopo
- Decisões de tese, posicionamento, portfólio, operação, arquitetura e go-to-market.

## Não-escopo
- Tarefas táticas do dia a dia sem impacto estratégico.

## Decisões

### 2026-01-16 — DL-2026-01-16-01 — Tese principal e alternativa (Fase 1)
- **Decisão**: Adotar como **tese principal** a Tese A (Copilotos de Operação para Backoffice) e como **alternativa** a Tese B (Suporte/Vendas com Conhecimento Vivo). Não priorizar Tese C como foco inicial.
- **Opções consideradas**:
  - **A**: Copilotos de Operação (backoffice financeiro/contábil/CS ops).
  - **B**: Suporte/Vendas com RAG + governança.
  - **C**: Devtool/kit de RAG/agents em produção.
- **Racional**:
  - **A** tem melhor combinação de **ROI claro**, ticket potencial maior e canal inicial menos dependente de ads/SEO (favorece outbound/parcerias).
  - **B** valida rápido e é fácil de demonstrar, mas sofre mais risco de commoditização/concorrência.
  - **C** tende a depender de canal de conteúdo/comunidade e ciclo mais longo no curto prazo.
- **Implicações**:
  - Estruturar oferta inicial como **wedge** (1–2 rotinas com ROI) para evitar consultoria infinita.
  - Medir tração por métricas objetivas em 14 dias antes de expandir escopo.
- **Links**:
  - `/docs/01-company/01-thesis.md`
  - `/docs/01-company/02-positioning.md`
  - `/docs/01-company/06-risk-register.md`

### 2026-01-16 — DL-2026-01-16-02 — Critérios de decisão em 14 dias (experimentos + métricas)
- **Decisão**: Decidir entre teses A e B com base em 3 critérios objetivos; vencerá quem bater **≥ 2 de 3** thresholds definidos.
- **Opções consideradas**:
  - Decisão por “feeling”/preferência técnica.
  - Decisão por canal (ads/SEO) sem validação de willingness-to-pay.
  - Decisão por LOIs e pilotos pagos com métricas de execução (escolhida).
- **Racional**:
  - Minimiza viés de confirmação e reduz risco de construir produto sem demanda pagante.
  - Força validação simultânea de **canal**, **dor/orçamento** e **viabilidade de entrega**.
- **Implicações**:
  - Exige cadência de outbound, demo e proposta padronizada.
  - Pode “matar” uma tese mesmo com boa tecnologia se não houver canal/urgência.
- **Thresholds**:
  - **Tração de canal**: resposta ≥ 8% e reuniões ≥ 3% por tese (outbound).
  - **Dor/orçamento**: ≥ 2 pilotos pagos ou LOI com valor e prazo por tese.
  - **Viabilidade**: primeiro valor ≤ 14 dias e ≤ 2 integrações no piloto.
- **Links**:
  - `/docs/01-company/01-thesis.md#decisões`

### 2026-01-16 — DL-2026-01-16-03 — Portfólio inicial orientado a wedge (evitar dispersão)
- **Decisão**: Definir um portfólio inicial com **1 oferta “core” (wedge)** alinhada à Tese A, mais **1 oferta alternativa** alinhada à Tese B e **utilitários internos** (IA-First) que acelerem entrega e virem ativos reutilizáveis; evitar lançar múltiplas ofertas externas ao mesmo tempo.
- **Opções consideradas**:
  - Portfólio amplo (muitas ofertas) para “pegar o que vier”.
  - Portfólio mínimo com 1 oferta apenas.
  - Portfólio com 1 core + 1 alternativa + utilitários internos (escolhida).
- **Racional**:
  - Reduz risco de dispersão (foco) sem travar aprendizado paralelo.
  - Permite validar canal e WTP em 14 dias sem criar backlog infinito.
  - Utilitários internos aumentam velocidade e qualidade (IA-First) e podem virar produtos depois.
- **Implicações**:
  - Requer limites claros de escopo no piloto e critérios de “o que entra / o que não entra”.
  - Exige priorização por ICE + risco de canal antes de abrir novas ofertas.
- **Links**:
  - `/docs/01-company/03-portfolio.md`

### 2026-01-16 — DL-2026-01-16-04 — Company OS (Fase 2) adotado como padrão operacional
- **Decisão**: Adotar um **Company OS IA-First** com 2 fundadores e portfólio em camadas (core + satélites), com processos padrão para operação, intake, entrega e rituais.
- **Opções consideradas**:
  - Operar “ad hoc” (processos informais) até ter 5+ clientes.
  - Processos pesados tipo enterprise desde o dia 1.
  - Processos leves, auditáveis e orientados por métricas (escolhida).
- **Racional**:
  - Reduz dispersão e risco de projetos “sem dono”.
  - Permite escala e qualidade com equipe pequena.
  - Mantém IA-First como vantagem operacional (velocidade + consistência).
- **Implicações**:
  - Exige disciplina semanal (rituais) e registro de decisões.
  - Exige templates e Definition-of-Done para evitar “quase pronto”.
- **Links**:
  - `/docs/02-ops/01-operating-model.md`
  - `/docs/02-ops/02-intake-process.md`
  - `/docs/02-ops/03-delivery-process.md`
  - `/docs/02-ops/04-weekly-rituals.md`

### 2026-01-16 — DL-2026-01-16-05 — Intake padronizado com score ICE + risco (canal e entrega)
- **Decisão**: Todo projeto/lead entra via **Intake** com triagem e score **ICE + risco** (canal e execução), gerando decisão Go/No-Go e registro no Decision Log quando necessário.
- **Opções consideradas**:
  - Priorizar por “urgência do cliente” e volume de pedidos.
  - Priorizar só por ICE (Impacto, Confiança, Esforço).
  - ICE + risco de canal + risco de entrega (escolhida).
- **Racional**:
  - Evita cair em canais instáveis (ads/SEO/plataformas) cedo demais.
  - Evita projetos com integrações/dados inviáveis para 2 founders.
- **Implicações**:
  - Alguns “bons” pedidos serão recusados por risco/escopo.
  - Requer formulário mínimo e checklist de prontidão.
- **Links**:
  - `/docs/02-ops/02-intake-process.md`

### 2026-01-16 — DL-2026-01-16-06 — Precificação inicial: setup + mensalidade (com limites e medição)
- **Decisão**: Adotar **setup + mensalidade** como padrão (sem cobrança por hora), com **limites explícitos** (integrações, volume, ambientes) e métricas de valor/custo desde o piloto.
- **Opções consideradas**:
  - Cobrança por hora (consultoria).
  - “Só mensalidade” desde o dia 1.
  - Setup + mensalidade com escopo fechado e limites (escolhida).
- **Racional**:
  - Protege contra R-001 (escopo) e R-008 (embalagem confusa).
  - Mantém previsibilidade de caixa e permite financiar integrações.
  - Força disciplina de instrumentação (custo LLM/infra) para evitar unit economics ocultos.
- **Implicações**:
  - Precisa de catálogo de limites e “o que acontece quando estoura limite”.
  - Exige definição de métricas mínimas por oferta (A1/B1).
- **Links**:
  - `/docs/01-company/04-pricing.md`

### 2026-01-16 — DL-2026-01-16-07 — Backlog orientado por épicos (core-first) + utilitários
- **Decisão**: Organizar execução em **épicos** alinhados ao portfólio (A1 core, B1 alternativa, U1–U3 utilitários) com prioridade por **ICE + risco** e WIP limitado.
- **Opções consideradas**:
  - Backlog por features soltas.
  - Backlog por épicos com DoD e métricas (escolhida).
- **Racional**:
  - Reduz troca de contexto e melhora rastreabilidade (decisão → entrega → métricas).
  - Facilita “core-first” sem bloquear aprendizado paralelo.
- **Implicações**:
  - Todo épico precisa de DoD e métricas de sucesso.
- **Links**:
  - `/docs/06-backlog/epics.md`

### 2026-01-16 — DL-2026-01-16-08 — GTM inicial: outbound + parcerias (evitar dependência de ads/SEO)
- **Decisão**: Adotar **outbound** como canal primário nas primeiras 2–6 semanas, complementado por **parcerias** (ex.: BPO/contabilidade para A1; consultorias CS para B1). Ads/SEO ficam como canal secundário até validação de ICP e unit economics.
- **Opções consideradas**:
  - Ads como canal principal desde o início.
  - Conteúdo/SEO como canal principal desde o início.
  - Outbound + parcerias como canal principal (escolhida).
- **Racional**:
  - Reduz risco de canal (R-004) e acelera aprendizado com baixo custo.
  - Permite testar ICP/wedge/preço em ciclos curtos e com feedback direto.
- **Implicações**:
  - Exige disciplina diária e scripts padronizados.
  - Depende de boa segmentação e entregabilidade para evitar reputação negativa.
- **Links**:
  - `/docs/01-company/05-gtm.md`

### 2026-01-16 — DL-2026-01-16-09 — Experimento EXP-001 (14 dias): outbound para validar wedge/ICP/preço
- **Decisão**: Executar um experimento de 14 dias de outbound com **métricas/thresholds** para validar: (1) dor e urgência, (2) WTP (piloto pago/LOI), (3) viabilidade do wedge com ≤2 integrações.
- **Opções consideradas**:
  - Construir MVP antes de falar com clientes.
  - Fazer entrevistas sem oferta/CTA.
  - Outbound com oferta de piloto e thresholds (escolhida).
- **Racional**:
  - Evita construir sem demanda pagante e cria comparabilidade entre teses (A1 vs B1).
  - Gera sinais rápidos de canal e objeções reais.
- **Implicações**:
  - Precisa de tracking rigoroso e rotina diária.
  - Requer ajuste de mensagem nas primeiras 48h com base em respostas.
- **Links**:
  - `/docs/05-research/experiments-14d/EXP-001-outbound.md`

### 2026-01-16 — DL-2026-01-16-10 — Portal institucional: sitemap mínimo focado em conversão
- **Decisão**: Definir sitemap do portal com **foco em conversão** (diagnóstico/piloto) e estrutura mínima: Home, Produto (A1/B1), Serviços (Implantação/Otimização), Sobre, Contato, FAQ, Privacidade/Termos.
- **Opções consideradas**:
  - Portal amplo com blog, cases, múltiplas landing pages.
  - Portal mínimo sem páginas de produto (só contato).
  - Portal mínimo focado em conversão com páginas por oferta (escolhida).
- **Racional**:
  - Reduz tempo de implementação e mantém foco em leads qualificados.
  - Permite testar copy e CTA antes de investir em conteúdo/blog.
  - Sitemap pode expandir após validação de ICP e wedge.
- **Implicações**:
  - Não terá blog/conteúdo no v1 (menos SEO orgânico, mas menos overhead).
  - Depende de outbound como canal primário até validar conversão do portal.
- **Links**:
  - `/docs/04-portal/01-sitemap.md`

### 2026-01-16 — DL-2026-01-16-11 — Copy do portal: tom profissional, pragmático, CTA para diagnóstico
- **Decisão**: Adotar copy em **PT-BR**, tom **profissional e pragmático** (sem hype/buzzwords), com CTA principal para **diagnóstico gratuito de 15 min** e CTA secundário para **proposta de piloto**.
- **Opções consideradas**:
  - Copy com linguagem de startup/tech (hype, jargões).
  - Copy minimalista sem benefícios/diferenciais.
  - Copy pragmática com benefícios claros, limites explícitos e CTA de conversão (escolhida).
- **Racional**:
  - Alinhada ao ICP (decisores de operação, não early adopters de tech).
  - Reduz objeções mostrando limites e pré-requisitos upfront.
  - CTA de diagnóstico qualifica leads antes de proposta comercial.
- **Implicações**:
  - Precisa validar copy com 3–5 leads do outbound antes de implementar.
  - [OPEN] Decidir se exibe preços no site ou só em proposta.
- **Links**:
  - `/docs/04-portal/02-copy.md`

### 2026-01-16 — DL-2026-01-16-12 — Tracking do portal: GA4 + GTM + eventos mínimos de conversão
- **Decisão**: Adotar **GA4 + GTM** como stack de tracking obrigatório, com eventos mínimos: `page_view`, `cta_click`, `form_submit`, `call_booked`. Meta Pixel e LinkedIn Insight Tag ficam como opcionais (só se rodar ads nessas plataformas).
- **Opções consideradas**:
  - Apenas GA4 básico (sem eventos customizados).
  - Stack complexo (Mixpanel, Segment, etc.).
  - GA4 + GTM com eventos customizados mínimos (escolhida).
- **Racional**:
  - Gratuito, robusto e suficiente para fase de validação.
  - Eventos customizados permitem medir funil completo (visitante → lead → call → proposta).
  - GTM facilita iteração sem deploy.
- **Implicações**:
  - Precisa implementar banner de consentimento (LGPD).
  - Precisa integrar formulário com CRM para tracking pós-conversão.
- **Links**:
  - `/docs/04-portal/04-tracking.md`

### 2026-01-16 — DL-2026-01-16-13 — Stack e arquitetura do Core Hub (MVP)
- **Decisão**: Adotar **FastAPI + Celery + LangChain/LangGraph + Postgres + Redis + Qdrant + MinIO** com multi-tenancy por `tenant_id` e Docker Compose no MVP (K8s v1+).
- **Opções consideradas**:
  - Node/TS backend; K8s desde o dia 1.
  - Arquitetura monolítica sem fila.
  - Stack Python com fila e componentes mínimos (escolhida).
- **Racional**:
  - Alinhado à experiência do time e ao uso intensivo de IA/LLM.
  - Fila necessária para fluxos assíncronos e HIL.
  - Compose reduz tempo de setup e é suficiente para 1–5 clientes.
- **Implicações**:
  - Precisa de disciplina de multi-tenant (tenant_id em todas as queries).
  - Migração planejada para K8s ao escalar (v1+).
- **Links**:
  - `/docs/03-products/core-hub/03-architecture.md`

### 2026-01-16 — DL-2026-01-16-14 — API REST com JWT + cursor e HIL unificado
- **Decisão**: API REST JSON com JWT + refresh em cookie httpOnly, paginação cursor-based e endpoints dedicados para HIL/approvals e auditoria.
- **Opções consideradas**:
  - GraphQL.
  - REST sem cursor e sem endpoint unificado de aprovação.
  - REST com cursor e HIL unificado (escolhida).
- **Racional**:
  - Simplicidade para frontend e integrações; contrato claro (OpenAPI).
  - Cursor evita problemas de paginação sob mudança de dados.
  - HIL unificado facilita UI e governança.
- **Implicações**:
  - Precisa de rate limiting por tenant.
  - Batch-approve com limites para evitar abuso.
- **Links**:
  - `/docs/03-products/core-hub/04-api.md`

### 2026-01-16 — DL-2026-01-16-15 — Dados e governança: retenção, PII e audit log
- **Decisão**: Multi-tenant por `tenant_id`, audit log append-only (5 anos), retenção de arquivos 180 dias, dados operacionais 24 meses [OPEN], PII minimizada e mascarada em logs.
- **Opções consideradas**:
  - Banco por tenant (custo alto).
  - Retenção indefinida.
  - Retenção limitada + mask + purge periódico (escolhida).
- **Racional**:
  - Equilíbrio entre custo, LGPD e simplicidade operacional.
  - Audit log imutável suporta segurança e troubleshooting.
- **Implicações**:
  - Jobs de purge e políticas de backup/restauração.
  - Máscara de PII em logs e tracing de LLM.
- **Links**:
  - `/docs/03-products/core-hub/05-data.md`

### 2026-01-16 — DL-2026-01-16-16 — LLMOps com HIL por default e gates de custo/qualidade
- **Decisão**: HIL obrigatório para ações sensíveis; validação de schema; caching; versionamento de prompts; métricas de latência/custo/qualidade com thresholds; incident playbook.
- **Opções consideradas**:
  - Auto-aprovação ampla sem HIL.
  - Observabilidade mínima sem custo/latência.
  - HIL default + observabilidade + gates (escolhida).
- **Racional**:
  - Reduz risco de ações erradas (R-006) e custo fora de controle (R-012).
  - Permite evoluir prompts/modelos com segurança.
- **Implicações**:
  - Requer dataset de avaliação e tracing de LLM.
  - Precisa definir ferramenta de observabilidade LLM [OPEN].
- **Links**:
  - `/docs/03-products/core-hub/06-llmops.md`

### 2026-01-16 — DL-2026-01-16-17 — Qualidade e release: LLM eval como gate + trunk-based
- **Decisão**: Pirâmide de testes (unit, integração, contrato, E2E, LLM eval), LLM eval como gate de promoção, trunk-based + SemVer, checklists de smoke e rollback com feature flags.
- **Opções consideradas**:
  - Sem gate de LLM; apenas testes manuais.
  - Gitflow pesado com releases longas.
  - Trunk-based + gates automáticos (escolhida).
- **Racional**:
  - Time pequeno precisa de cadência rápida com segurança.
  - LLM eval previne regressões silenciosas de qualidade/custo.
- **Implicações**:
  - Pipelines devem rodar eval curta em cada release.
  - Feature flags necessárias para rollback seguro.
- **Links**:
  - `/docs/03-products/core-hub/07-testing.md`
  - `/docs/03-products/core-hub/08-release.md`

### 2026-01-16 — DL-2026-01-16-18 — Plano de sprints do MVP (3 sprints, 1 fluxo)
- **Decisão**: Executar 3 sprints semanais focadas em 1 fluxo (cobrança) com HIL, antes de expandir para outros fluxos.
- **Opções consideradas**:
  - Atacar 3 fluxos em paralelo.
  - Sprints longas (>2 semanas).
  - 3 sprints curtas e foco em 1 fluxo (escolhida).
- **Racional**:
  - Minimiza risco de dispersão (R-001/R-007) e permite medir resultado rápido.
  - Estrutura incremental: fundações → integrações/observabilidade → piloto.
- **Implicações**:
  - Outras rotinas (conciliação/AP) ficam no backlog até fechar piloto.
  - Checklist de piloto/relatório semanal obrigatório.
- **Links**:
  - `/docs/06-backlog/mvp-sprints.md`

### 2026-01-16 — DL-2026-01-16-19 — Portal: framework de UI e simplicidade visual
- **Decisão**: Usar UI simples com ícones leves, grid 12 col, cores sóbrias e CTA visível; evitar ilustrações “hype”. Framework recomendado: Vue 3 + Tailwind; ícones: Heroicons.
- **Opções consideradas**:
  - Vue 3 + Tailwind + Heroicons (recomendada).
  - Angular + Tailwind.
  - React + Tailwind.
- **Racional**:
  - Time já tem experiência; entrega mais rápida e menor atrito.
  - Visual limpo reforça confiança e foco em conversão.
- **Implicações**:
  - Ajustar identidade final (cores/logotipo) ainda [OPEN].
  - Se time preferir Angular, manter Tailwind para velocidade.
- **Links**:
  - `/docs/04-portal/03-design-notes.md`

### 2026-01-16 — DL-2026-01-16-20 — Contact Ops: fluxo e ferramental MVP
- **Decisão**: Fluxo de contato simples com resposta ≤24h úteis, 3 toques de follow-up e qualificação curta; armazenar em planilha/Notion/CRM leve; alerta de `form_submit` obrigatório.
- **Opções consideradas**:
  - Planilha/Notion (recomendada para MVP).
  - Pipedrive básico.
  - HubSpot free.
- **Racional**:
  - Velocidade de implantação e baixo atrito para time de 2 pessoas.
  - Mantém rastreabilidade mínima e integra com Intake depois.
- **Implicações**:
  - Definir política de WhatsApp/LinkedIn (consentimento) [OPEN].
  - Implementar alerta imediato (e-mail/Slack) no submit.
- **Links**:
  - `/docs/04-portal/05-contact-ops.md`

## Riscos
Ver `/docs/01-company/06-risk-register.md`.

## Próximos passos
- Executar os experimentos de 14 dias descritos em `/docs/01-company/01-thesis.md`.
- Registrar novas decisões e mudanças de direção aqui, sem apagar histórico.


