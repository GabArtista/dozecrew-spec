---
title: KPIs da Empresa - Doze Crew
status: active
version: 1.0.0
owners:
  - Gabriel
  - Miguel
updated: 2026-01-17
tags:
  - kpis
  - metrics
  - enterprise
---

# KPIs da Empresa - Doze Crew

## Contexto

Este documento define os KPIs estratégicos da empresa Doze Crew como um todo.

> **Escopo**: Métricas de NEGÓCIO e EMPRESA, não de projetos específicos.

## Categorias de KPIs

```
┌─────────────────────────────────────────────────────────────┐
│                    KPIs da Empresa                          │
├─────────────────┬─────────────────┬─────────────────────────┤
│   Financeiros   │   Comerciais    │      Operacionais       │
├─────────────────┼─────────────────┼─────────────────────────┤
│ MRR/ARR         │ Leads           │ Tempo de Entrega        │
│ Receita         │ Conversão       │ Utilização              │
│ Margem          │ Churn           │ Satisfação              │
│ CAC/LTV         │ Pipeline        │ Qualidade               │
└─────────────────┴─────────────────┴─────────────────────────┘
```

---

## KPIs Financeiros

### MRR (Monthly Recurring Revenue)

| Atributo | Valor |
|----------|-------|
| Meta Q1 | R$ 10.000 |
| Meta Q2 | R$ 25.000 |
| Meta Q4 | R$ 50.000 |
| Frequência | Mensal |
| Owner | Miguel |

**Fórmula**: Soma de todas as receitas recorrentes mensais.

---

### Receita Total

| Atributo | Valor |
|----------|-------|
| Meta Ano 1 | R$ 300.000 |
| Frequência | Mensal |
| Owner | Miguel |

**Composição**:
- Receita recorrente (SaaS)
- Receita de serviços (setup + consultoria)
- Receita de utilitários

---

### Margem Bruta

| Atributo | Valor |
|----------|-------|
| Meta | > 60% |
| Frequência | Mensal |
| Owner | Gabriel |

**Fórmula**: (Receita - Custo Direto) / Receita × 100

**Custos Diretos**:
- APIs de IA (OpenAI, Anthropic)
- Infraestrutura (cloud, hosting)
- Ferramentas SaaS essenciais

---

### CAC (Custo de Aquisição de Cliente)

| Atributo | Valor |
|----------|-------|
| Meta | < R$ 2.000 |
| Frequência | Mensal |
| Owner | Miguel |

**Fórmula**: (Marketing + Vendas) / Novos Clientes

---

### LTV (Lifetime Value)

| Atributo | Valor |
|----------|-------|
| Meta | > R$ 12.000 |
| Frequência | Trimestral |
| Owner | Miguel |

**Fórmula**: ARPU × Tempo Médio de Retenção (meses)

**Meta LTV/CAC**: > 3x

---

## KPIs Comerciais

### Leads Qualificados (MQL)

| Atributo | Valor |
|----------|-------|
| Meta Mensal | 20 |
| Frequência | Semanal |
| Owner | Gabriel |

**Critérios de Qualificação**:
- ICP correto (PME 10-100 func)
- Dor identificada
- Budget disponível

---

### Taxa de Conversão

| Funil | Meta |
|-------|------|
| Lead → MQL | 30% |
| MQL → Diagnóstico | 40% |
| Diagnóstico → Piloto | 50% |
| Piloto → Cliente | 60% |

---

### Churn Rate

| Atributo | Valor |
|----------|-------|
| Meta | < 5% mensal |
| Frequência | Mensal |
| Owner | Miguel |

**Fórmula**: Clientes Perdidos / Clientes Início do Mês × 100

---

### Pipeline Value

| Atributo | Valor |
|----------|-------|
| Meta | 3x MRR Target |
| Frequência | Semanal |
| Owner | Gabriel |

---

## KPIs Operacionais

### Tempo Médio de Entrega

| Tipo | Meta |
|------|------|
| Diagnóstico | 5 dias |
| MVP/Piloto | 4 semanas |
| Implementação Full | 8 semanas |

---

### Taxa de Utilização

| Atributo | Valor |
|----------|-------|
| Meta | 70% |
| Frequência | Semanal |
| Owner | Gabriel |

**Fórmula**: Horas Faturáveis / Horas Disponíveis × 100

---

### NPS (Net Promoter Score)

| Atributo | Valor |
|----------|-------|
| Meta | > 50 |
| Frequência | Trimestral |
| Owner | Miguel |

**Fórmula**: % Promotores - % Detratores

---

### Taxa de Entregas no Prazo

| Atributo | Valor |
|----------|-------|
| Meta | > 90% |
| Frequência | Mensal |
| Owner | Gabriel |

---

## Dashboard

### Visualização Sugerida

```
┌─────────────────────────────────────────────────────────────┐
│                   Dashboard Executivo                        │
├─────────────┬─────────────┬─────────────┬───────────────────┤
│    MRR      │   Leads     │   Churn     │       NPS         │
│  R$ XX.XXX  │     XX      │    X.X%     │       XX          │
│   ↑ 15%     │   ↑ 10%     │   ↓ 0.5%    │      ↑ 5          │
├─────────────┴─────────────┴─────────────┴───────────────────┤
│                    Pipeline por Estágio                      │
│ [====] Lead  [====] MQL  [===] Diag  [==] Piloto [=] Cliente│
├─────────────────────────────────────────────────────────────┤
│                   Utilização da Equipe                       │
│ Gabriel [========] 80%   Miguel [=======] 70%               │
└─────────────────────────────────────────────────────────────┘
```

### Ferramentas Recomendadas

| Ferramenta | Uso |
|------------|-----|
| Google Sheets | Tracking inicial |
| Notion | Dashboard visual |
| Metabase | BI self-hosted |
| Power BI | Análises avançadas |

---

## Revisão

### Frequência

| Tipo | Frequência | Participantes |
|------|------------|---------------|
| Operacional | Semanal | Gabriel + Miguel |
| Estratégico | Mensal | Gabriel + Miguel |
| Board | Trimestral | Gabriel + Miguel |

### Processo

1. Coletar dados até sexta-feira
2. Atualizar dashboard segunda de manhã
3. Revisão na weekly de segunda-feira
4. Ações corretivas se fora da meta

---

## Metas por Trimestre

### Q1 2026

| KPI | Meta |
|-----|------|
| MRR | R$ 10.000 |
| Clientes | 5 |
| NPS | > 40 |
| Churn | < 10% |

### Q2 2026

| KPI | Meta |
|-----|------|
| MRR | R$ 25.000 |
| Clientes | 12 |
| NPS | > 50 |
| Churn | < 5% |

---

## Histórico

| Data | Alteração |
|------|-----------|
| 2026-01-17 | Documento criado |

