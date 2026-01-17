---
title: Operating Model (Company OS)
status: draft
owners:
  - Gabriel
  - Miguel
updated: 2026-01-16
links:
  - /docs/00-index/decision-log.md
  - /docs/01-company/01-thesis.md
  - /docs/01-company/03-portfolio.md
  - /docs/02-ops/02-intake-process.md
  - /docs/02-ops/03-delivery-process.md
  - /docs/02-ops/04-weekly-rituals.md
  - /docs/02-ops/05-templates/TPL-001-intake-form.md
tags:
  - ops
  - operating-model
  - ia-first
---

## Contexto
Empresa IA-First com 2 fundadores e portfólio em camadas:
- **Core (A1)**: Copiloto de Operação para backoffice (wedge)
- **Alternativa (B1)**: Conhecimento vivo + QA para suporte/vendas
- **Utilitários internos (U1–U3)**: integrações/ETL, avaliação/observabilidade, guardrails/human-in-the-loop

## Objetivo
Definir como a empresa opera ponta a ponta (vendas, entrega, produto, suporte e finanças), com donos claros, handoffs mínimos e uso de IA com guardrails.

## Escopo
- Mapa de operações e responsabilidades.
- Artefatos mínimos e handoffs.
- Métricas por operação.

## Não-escopo
- Organograma futuro (contratações) e políticas de RH completas.

## Mapa de Operações (end-to-end)

### 1) Vendas (GTM)
- **Objetivo**: gerar pipeline qualificado e converter em piloto pago com escopo fechado.
- **Entradas**: leads (outbound/parcerias) + problemas relatados.
- **Saídas**:
  - Intake completo + score ICE+risco
  - Proposta de piloto (SOW) + preço + limites
  - Go/No-Go registrado
- **DRI padrão**: Miguel (com apoio técnico do Gabriel quando necessário)
- **Métricas**:
  - resposta %, reuniões %, taxa de proposta, taxa de piloto pago
  - tempo do 1º contato → piloto assinado
  - motivo de perda (taxonomia) [OPEN]

### 2) Entrega (Delivery)
- **Objetivo**: executar Discovery → MVP → Piloto → Escala com qualidade, segurança e prazos.
- **Entradas**: SOW + checklist de prontidão (dados/integr. /compliance) + metas do piloto.
- **Saídas**:
  - MVP funcional em staging + métricas instrumentadas
  - Piloto com resultados e relatório
  - Plano de escala (ou encerramento)
- **DRI padrão**: Gabriel (engenharia/dados) + Miguel (produto/UX)
- **Métricas**:
  - lead time por etapa, % entregas no prazo
  - custo por execução (infra/LLM) [OPEN]
  - incidentes e retrabalho

### 3) Produto (Product)
- **Objetivo**: transformar aprendizados de pilotos em componentes reutilizáveis (core + utilitários) priorizados por ICE+risco.
- **Entradas**: feedback de pilotos, métricas, incidentes, pedidos.
- **Saídas**:
  - backlog priorizado
  - decisões de escopo (inclui “não fazer”)
  - definição e evolução de wedge
- **DRI padrão**: Miguel (priorização/UX) + Gabriel (viabilidade técnica)
- **Métricas**:
  - ciclo de aprendizado (hipótese → experimento → decisão)
  - adoção de componentes reutilizáveis (% do trabalho reaproveitado) [OPEN]

### 4) Suporte/Customer Success
- **Objetivo**: garantir resultado do piloto e reduzir risco operacional do cliente.
- **Entradas**: dúvidas, incidentes, pedidos de mudança.
- **Saídas**:
  - respostas e ajustes dentro do escopo
  - registro de incidentes + ações corretivas
  - renovações/expansões
- **DRI padrão**: Miguel
- **Métricas**:
  - tempo de resposta, incidentes/semana
  - saúde do piloto (métricas-alvo atingidas?)

### 5) Finanças/Operação interna
- **Objetivo**: caixa saudável e previsibilidade.
- **Entradas**: contratos, custos, notas/faturamento.
- **Saídas**:
  - DRE simplificada mensal [OPEN]
  - controle de caixa e runway
- **DRI padrão**: Miguel
- **Métricas**:
  - MRR/receita de setup, margem bruta estimada, runway

## Handoffs e Artefatos Mínimos
- **Lead → Intake**: `TPL-001` (form) + score (ICE+risco)
- **Intake → Go/No-Go**: decisão registrada + SOW padrão
- **Go → Delivery**: checklist de prontidão + metas do piloto + DoD por etapa
- **Delivery → Produto**: post-mortem do piloto + itens de padronização (utilitários)

## Decisões
- **Decidido**: usar Company OS leve com processos padronizados e auditáveis.
- **[OPEN]**: taxonomia de motivos de perda e categorias de incidentes.

## Riscos
Ver Risk Register:
- R-009 (overhead de processo), R-010 (burnout), R-011 (handoff).

## Próximos passos
- Adotar templates padrão em todos os novos leads/projetos.
- Definir o “dashboard semanal” e fonte única de verdade (planilha/Notion/Git) [OPEN].
- Rodar 2 semanas e ajustar o OS com base em métricas (cortar o que não gera decisão).



