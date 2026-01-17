---
title: Tese da Empresa (Fase 1)
status: draft
owners:
  - Gabriel
  - Miguel
updated: 2026-01-16
links:
  - /docs/00-index/decision-log.md
  - /docs/01-company/02-positioning.md
  - /docs/01-company/03-portfolio.md
  - /docs/01-company/06-risk-register.md
tags:
  - company
  - thesis
  - strategy
  - ia-first
---

## Contexto
Equipe:
- Gabriel: IA/Engenharia de Dados/Automação/Backend (Python, ETL, RAG, LangChain, Qdrant, Docker etc.)
- Miguel: Full-stack + produto (JS, Angular/Vue, C# etc.), experiência em produto real

Meta final do projeto: empresa idealizada + sistema operacional (processos e rotinas) + portfólio + portal institucional + SpecKit completo para execução.

Suposições:
- **Geografia**: Brasil/LatAm [OPEN]
- **Canal inicial**: outbound + parcerias (sem depender de ads/SEO no início) [OPEN]
- **Modelo**: pilots curtos (14–30 dias) com ROI claro [OPEN]

## Objetivo
Definir 3 teses candidatas e selecionar 1 tese principal + 1 alternativa, com critérios objetivos de decisão em 14 dias.

## Escopo
- Definição de tese (categoria, ICP, dor, promessa, diferencial, moat, risco principal).
- Recomendação e critérios de escolha em 14 dias (experimentos + métricas).

## Não-escopo
- Roadmap detalhado de produto.
- Arquitetura técnica completa.
- Precificação final (apenas faixas iniciais).

## Teses candidatas

### Tese A — Copilotos de Operação para Backoffice (Financeiro/Contábil/CS Ops)
- **Categoria**: Produto + serviço (implantação) de automação operacional com agentes + RAG + integrações
- **ICP**:
  - PME (20–200 funcionários) com alto volume de rotinas (financeiro/operacional)
  - Escritórios contábeis e BPO financeiro com volume e SLAs
- **Dor**:
  - Rotinas repetitivas e manuais (planilhas, e-mail/WhatsApp, conciliações)
  - Erros, retrabalho, dependência de pessoas-chave, baixa auditabilidade
- **Promessa**:
  - “Em 30 dias, reduzir X% do tempo gasto em rotinas repetitivas e aumentar previsibilidade (SLA + trilha auditável) sem trocar seus sistemas”
- **Diferencial**:
  - IA aplicada **à execução** (não só respostas): RAG sobre SOPs + conectores + human-in-the-loop + observabilidade (o que foi feito e por quê)
- **Moat (defensabilidade)**:
  - Playbooks por vertical (AP/AR, conciliação, cobrança, emissão, reconciliação)
  - Conectores reutilizáveis + know-how de dados/ETL
  - Loop de feedback (avaliação + logs) virando dataset proprietário
- **Risco principal**:
  - Virar “consultoria infinita” (cada cliente um caos), reduzindo margem e escala
- **Trade-offs**:
  - Mais sob medida = mais valor no curto prazo e menos escala; mais padrão = mais escala e mais concorrência.

### Tese B — Suporte e Vendas com Conhecimento Vivo (Omnichannel RAG + QA)
- **Categoria**: SaaS de atendimento/enablement (assistente para suporte e pré-vendas) + governança de qualidade
- **ICP**:
  - SaaS B2B e e-commerce com suporte em PT-BR (Zendesk/Intercom/WhatsApp)
  - Times de CS/Support com > 5 pessoas e alto volume de tickets
- **Dor**:
  - Respostas inconsistentes; base de conhecimento desatualizada; onboarding lento
  - Alto TMA; baixa deflexão; perda de receita por dúvidas repetidas
- **Promessa**:
  - “Reduzir TMA e aumentar consistência/CSAT com respostas citadas e auditáveis; transformar docs soltas em conhecimento operacional”
- **Diferencial**:
  - Governança/qualidade: citações, detecção de alucinação, políticas por segmento de cliente, auditoria, métricas de deflexão
- **Moat (defensabilidade)**:
  - Engine de avaliação contínua + rotulagem ativa com tickets reais
  - Conectores para canais BR (WhatsApp) e bom PT-BR
- **Risco principal**:
  - Mercado commoditizado e competitivo (difícil diferenciar apenas com “RAG para suporte”)
- **Trade-offs**:
  - “Plugar e funcionar” facilita venda, mas reduz diferenciação; governança aumenta venda consultiva e ciclo.

### Tese C — RAG & Automação em Produção (Kit + plataforma para times dev)
- **Categoria**: Utilitário/devtool (self-hosted) + serviços de implantação (LLMOps)
- **ICP**:
  - Times de engenharia (10–100 devs) em empresas que precisam de RAG/agents com segurança (fintech/saúde/indústria/SaaS)
- **Dor**:
  - Fazer demo é fácil; produzir com avaliação, custo controlado, segurança, observabilidade e atualização contínua é difícil
- **Promessa**:
  - “Em 14 dias, RAG em produção com avaliação, monitoramento, custo por resposta e pipeline de atualização — sem caixa-preta”
- **Diferencial**:
  - Foco production-grade (templates Docker + Qdrant + avaliação automatizada + tracing + guardrails)
- **Moat (defensabilidade)**:
  - Playbooks de arquitetura + automações de deploy + boas práticas incorporadas
  - Autoridade técnica via conteúdo (vira canal no médio prazo)
- **Risco principal**:
  - Dependência de canal de conteúdo/SEO/comunidade e/ou ciclos longos
- **Trade-offs**:
  - Melhor escala no longo prazo; menor previsibilidade no curto prazo.

## Decisões
- **Tese principal (decidido)**: **Tese A**
- **Tese alternativa (decidido)**: **Tese B**
- **Não priorizar (decidido)**: Tese C como foco inicial

## Critérios objetivos para decidir em 14 dias (experimentos + métricas)
Regra: a tese “vence” se bater **≥ 2 de 3** critérios abaixo.

### Critério 1 — Tração de canal (risco de canal baixo no curto prazo)
- **Outbound por tese**: 80–120 contatos (ICP qualificado)
- **Taxa de resposta**: ≥ 8%
- **Taxa de reuniões**: ≥ 3% dos contatos
- **Esforço por reunião marcada**: ≤ 90 min de esforço total

### Critério 2 — Dor + orçamento (willingness-to-pay real)
- **Meta**: ≥ 2 pilotos pagos **OU** LOIs com valor e prazo por tese
- **Ticket inicial (faixas)**:
  - **Tese A**: setup R$ 5k–20k + R$ 2k–10k/mês
  - **Tese B**: R$ 1k–6k/mês + setup leve
- **Objeções**:
  - Registrar objeções “matadoras” e se são contornáveis em ≤ 30 dias

### Critério 3 — Viabilidade de entrega (sem virar projeto infinito)
- **Primeiro valor**: ≤ 14 dias
- **Integrações**: ≤ 2 sistemas no piloto
- **Métrica do piloto**:
  - **Tese A**: horas poupadas/semana + redução de erros + SLA/auditoria
  - **Tese B**: deflexão + TMA + CSAT + taxa de aprovação humana

## Experimentos (plano 14 dias)

### E1 — Outbound estruturado (Dias 1–10)
- **A (Backoffice)**: donos/COO/financeiro + donos de BPO/contabilidade
- **B (CS/Support)**: Head de CS/Support em SaaS/e-commerce
- **Entregáveis**:
  - 1 landing page por tese (1 tela) + 1 deck curto (5 slides) [OPEN]
  - Script de abordagem + sequência (e-mail/LinkedIn/WhatsApp) [OPEN]

### E2 — Demo “quase real” (Dias 3–10)
- **A**: 1 fluxo automatizado com human-in-the-loop (ex.: e-mails/boletos → classificação → tarefa + log auditável)
- **B**: base de conhecimento + respostas citadas + painel de aprovação/feedback
- **Entregáveis**:
  - Vídeo de 3 minutos por tese [OPEN]
  - Ambiente navegável (staging)

### E3 — Proposta de piloto pago padronizada (Dias 7–14)
- **Entregáveis**:
  - Proposta 1 página (escopo fechado + limites) [OPEN]
  - Checklist de prontidão de dados + segurança [OPEN]

## Riscos
Ver `/docs/01-company/06-risk-register.md` (R-001 a R-006).

## Próximos passos
- Fechar as suposições [OPEN] (geografia, canal, ICP inicial) com 3 entrevistas rápidas por tese.
- Definir o wedge inicial da Tese A (1–2 rotinas) e o “diferencial mínimo” da Tese B (governança/qualidade).
- Iniciar E1 (outbound) e preparar E2 (demo) em paralelo.

## Changed/Deprecated
- 2026-01-16: adicionada referência ao portfólio em `/docs/01-company/03-portfolio.md` (sem alterar a tese aprovada).


