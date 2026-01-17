---
title: Portfólio (Produtos, Serviços e Utilitários)
status: draft
owners:
  - Gabriel
  - Miguel
updated: 2026-01-16
links:
  - /docs/01-company/01-thesis.md
  - /docs/00-index/decision-log.md
  - /docs/01-company/04-pricing.md
  - /docs/01-company/06-risk-register.md
tags:
  - company
  - portfolio
  - offers
  - ia-first
---

## Contexto
O portfólio define “o que vendemos” e “o que construímos”, alinhado às teses e limitado por foco/execução. Ele também organiza utilitários internos que aceleram a operação IA-First.

## Objetivo
Definir um portfólio inicial pragmático: 1 oferta core (wedge) para a tese principal (A), 1 oferta alternativa (B) e um conjunto mínimo de utilitários internos reutilizáveis.

## Escopo
- Ofertas externas (clientes): produto + serviços de implantação/piloto.
- Utilitários internos (aceleradores): componentes reaproveitáveis que reduzem esforço e risco.
- Critérios de priorização (ICE + risco de canal).

## Não-escopo
- Roadmap detalhado por quarter.
- Precificação final e contratos (apenas diretrizes e faixas quando necessário).

## Portfólio — Ofertas Externas (Go-to-market)

### Oferta A1 (CORE / WEDGE) — “Copiloto de Rotinas Financeiras” (Backoffice)
- **Alinha com**: Tese A
- **Forma**: piloto + implantação + assinatura
- **Problema-alvo**: rotinas repetitivas e auditabilidade (ex.: AP/AR, conciliação, cobrança) [OPEN: escolher 1–2 rotinas]
- **Entregável do piloto (14–30 dias)**:
  - 1 fluxo automatizado com human-in-the-loop
  - logs/trilha auditável + métricas de valor
  - integração com até 2 sistemas
- **Limites padrão (para manter escala)**:
  - até 2 integrações no piloto
  - 1 ambiente (staging) + 1 piloto (produção controlada) [OPEN]
  - volume inicial acordado (ex.: X execuções/dia) [OPEN]
- **Métrica de sucesso**:
  - horas poupadas/semana, redução de erros, SLA e tempo de ciclo
- **Riscos principais**:
  - R-001 (consultoria infinita), R-005 (integrações), R-006 (qualidade)
- **Trade-offs**:
  - Escopo fechado acelera ROI e escalabilidade; limita “abrangência” percebida na venda.

### Oferta B1 (ALTERNATIVA) — “Base de Conhecimento Viva + QA” (Suporte/Vendas)
- **Alinha com**: Tese B
- **Forma**: SaaS leve + setup
- **Problema-alvo**: inconsistência e baixa qualidade em respostas; base de conhecimento desatualizada
- **Entregável do piloto (14–30 dias)**:
  - respostas com citações + painel de aprovação/feedback
  - avaliação contínua (amostras) e relatórios de deflexão/TMA/CSAT
- **Limites padrão (para manter margem)**:
  - fontes/documentos iniciais (ex.: até N páginas/URLs) [OPEN]
  - volume de mensagens/tickets por mês (faixas) [OPEN]
- **Métrica de sucesso**:
  - deflexão, TMA, CSAT, taxa de aprovação humana
- **Riscos principais**:
  - R-002 (commoditização), R-003 (dados), R-006 (qualidade)
- **Trade-offs**:
  - Menor ticket tende a exigir volume; diferenciação depende de governança/qualidade.

### Oferta C1 (FUTURO / NÃO PRIORITÁRIA) — “RAG em Produção (Kit + Serviços)”
- **Alinha com**: Tese C
- **Status**: não priorizar como oferta principal no curto prazo; usar como ativo interno e, se necessário, como serviço premium pontual [OPEN]
- **Risco principal**: canal (conteúdo/comunidade) e ciclo mais longo (R-004)

## Portfólio — Utilitários Internos (IA-First)
Objetivo: reduzir esforço e risco por padrão (qualidade, observabilidade, segurança).

### U1 — “Kit de Integrações + ETL” (conectores reutilizáveis)
- **Uso**: acelerar pilotos da Oferta A1 e B1
- **Inclui**: conectores, validação de schema, jobs de ingestão e monitoramento
- **Risco mitigado**: R-005

### U2 — “Avaliação e Observabilidade LLM” (quality + cost)
- **Uso**: medir alucinação, custo por tarefa/resposta, regressões e confiança
- **Inclui**: tracing, conjunto de casos, métricas e painéis
- **Risco mitigado**: R-006

### U3 — “Guardrails + Human-in-the-loop” (segurança operacional)
- **Uso**: aprovações para ações sensíveis, níveis de confiança, trilha auditável
- **Risco mitigado**: R-003, R-006

## Priorização (ICE + risco de canal)
Regras:
- Priorizar iniciativas com **ROI explícito** e **canal controlável** (outbound/parcerias).
- Penalizar iniciativas com dependência de **ads/SEO/plataformas** no curto prazo.

Tabela inicial (estimativa; recalibrar após 14 dias):
- **A1 (CORE)**: Impacto Alto | Confiança Média/Alta | Esforço Médio | Risco de canal Baixo/Médio
- **B1 (Alternativa)**: Impacto Médio | Confiança Média | Esforço Médio | Risco de canal Médio
- **U1/U2/U3 (Interno)**: Impacto Alto (na velocidade/qualidade) | Confiança Alta | Esforço Médio | Risco de canal N/A

## Decisões
- **Decidido**: Portfólio inicial será “1 core + 1 alternativa + utilitários internos”; evitar múltiplas ofertas externas simultâneas.
- **[OPEN]**: Wedge da Oferta A1 (quais 1–2 rotinas iniciais).
- **[OPEN]**: Canal prioritário para Oferta B1 (WhatsApp vs Zendesk/Intercom primeiro).
- **[OPEN]**: Política de deployment (SaaS vs self-hosted) por ICP e requisito de compliance.
- **Decidido**: preços e pacotes ficam em `/docs/01-company/04-pricing.md` e são aplicados via SOW de piloto.

## Riscos
Ver `/docs/01-company/06-risk-register.md` (inclui R-007 e R-008).

## Próximos passos
- Escolher o wedge da Oferta A1 com base em 5 conversas rápidas (dor + volume + integração).
- Transformar U1/U2/U3 em checklist de implantação do piloto (não como “projeto paralelo”).
- Registrar decisões [OPEN] no Decision Log após os primeiros 10 contatos por tese.

## Changed/Deprecated
- 2026-01-16: adicionados limites padrão por oferta e link para o pricing (sem remover decisões aprovadas).


