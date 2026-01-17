---
title: Plano de Pesquisa Contínua
status: active
version: 1.0.0
owners:
  - Gabriel
  - Miguel
updated: 2026-01-17
tags:
  - research
  - plan
  - monitoring
  - routine
---

# Plano de Pesquisa Contínua

## 1. Visão Geral

### Objetivo

Manter a Doze Crew informada sobre:
- Movimentos de concorrentes
- Tendências de mercado
- Novas tecnologias
- Oportunidades de negócio

### Princípios

| Princípio | Descrição |
|-----------|-----------|
| **Consistência** | Rotina semanal, não esforço pontual |
| **Foco** | Priorizar o que impacta decisões |
| **Ação** | Cada insight deve gerar ação |
| **Documentação** | Registrar para referência futura |

---

## 2. Alertas Configurados

### Google Alerts

| Alerta | Query | Frequência |
|--------|-------|------------|
| Mercado | "automação financeira" OR "automação backoffice" | Diário |
| IA Brasil | "inteligência artificial" AND "PME" | Diário |
| Concorrentes | "UiPath" OR "Automation Anywhere" OR "Make.com" | Semanal |
| RAG/LLM | "RAG" OR "LangChain" OR "vector database" | Semanal |
| BPO | "BPO financeiro" OR "terceirização contábil" | Semanal |

### LinkedIn

| Tipo | O que monitorar | Frequência |
|------|-----------------|------------|
| Páginas | Concorrentes (Omie, TOTVS, Zenvia) | Semanal |
| Hashtags | #automação #IA #backoffice | Diário |
| Grupos | CFOs, gestores financeiros | Semanal |

### Outras Fontes

| Fonte | O que monitorar | Frequência |
|-------|-----------------|------------|
| Product Hunt | Novos produtos de automação/IA | Diário |
| Hacker News | Tech trends | Diário |
| TechCrunch | Funding, M&A | Semanal |
| Crunchbase | Startups BR em IA | Quinzenal |

---

## 3. Rotina de Pesquisa

### Diária (15 min)

| Horário | Atividade | Responsável |
|---------|-----------|-------------|
| Manhã | Verificar alertas Google | Gabriel |
| Manhã | Scan LinkedIn feed | Miguel |
| Tarde | Product Hunt / HN | Alternado |

### Semanal (1-2h)

| Dia | Atividade | Responsável | Output |
|-----|-----------|-------------|--------|
| Segunda | Review de alertas | Gabriel | Lista de insights |
| Quarta | Análise de concorrentes | Miguel | Update no 02-competitors.md |
| Sexta | Revisão de newsletters | Ambos | Discussão |

### Mensal (4h)

| Semana | Atividade | Output |
|--------|-----------|--------|
| 1 | Análise de tráfego (Similarweb) | Report |
| 2 | Review de ferramentas | Update 03-tools.md |
| 3 | Entrevistas com mercado | Notas |
| 4 | Revisão geral da pasta | Updates |

### Trimestral (1 dia)

| Atividade | Output |
|-----------|--------|
| Revisão completa de mercado | Update 01-market-analysis.md |
| Atualização de concorrentes | Update 02-competitors.md |
| Avaliação de oportunidades | Update 06-opportunities.md |
| Planejamento do próximo trimestre | Roadmap |

---

## 4. Fontes Prioritárias

### Tier 1 (Essencial)

| Fonte | Link | Frequência |
|-------|------|------------|
| Google Alerts | alerts.google.com | Diário |
| LinkedIn | linkedin.com | Diário |
| TLDR AI Newsletter | tldr.tech/ai | Diário |
| LangChain Blog | blog.langchain.dev | Semanal |
| Lenny's Newsletter | lennysnewsletter.com | Semanal |

### Tier 2 (Importante)

| Fonte | Link | Frequência |
|-------|------|------------|
| Product Hunt | producthunt.com | Diário |
| Hacker News | news.ycombinator.com | Diário |
| TechCrunch | techcrunch.com | Semanal |
| Stratechery | stratechery.com | Semanal |
| The Batch (Andrew Ng) | deeplearning.ai/the-batch | Semanal |

### Tier 3 (Nice to have)

| Fonte | Link | Frequência |
|-------|------|------------|
| arxiv AI | arxiv.org/list/cs.AI | Quinzenal |
| Gartner Blog | gartner.com/en/blog | Mensal |
| McKinsey Insights | mckinsey.com | Mensal |
| CB Insights | cbinsights.com | Mensal |

---

## 5. Templates de Registro

### Insight de Mercado

```markdown
## [DATA] - [TÍTULO]

**Fonte**: [link]
**Categoria**: Concorrente | Tendência | Oportunidade | Ameaça

### Resumo
[2-3 frases]

### Impacto para Doze Crew
- [ ] Alto
- [ ] Médio
- [ ] Baixo

### Ação Sugerida
[O que fazer com essa informação]

### Tags
#mercado #concorrente #tendencia
```

### Análise de Concorrente

```markdown
## [DATA] - Update [CONCORRENTE]

**Mudança identificada**: [descrição]
**Fonte**: [link]

### O que mudou
- Feature nova: [descrição]
- Preço: [mudança]
- Posicionamento: [mudança]

### Impacto
[Como afeta nosso posicionamento]

### Resposta sugerida
[Ação a tomar]
```

---

## 6. Métricas de Pesquisa

### KPIs do Processo

| Métrica | Meta | Frequência |
|---------|------|------------|
| Alertas revisados | 100% | Semanal |
| Insights documentados | 5+/semana | Semanal |
| Updates de docs | 2+/mês | Mensal |
| Entrevistas com mercado | 2/mês | Mensal |

### KPIs de Resultado

| Métrica | Meta | Frequência |
|---------|------|------------|
| Decisões baseadas em pesquisa | 50%+ | Mensal |
| Oportunidades identificadas | 3+/trimestre | Trimestral |
| Ameaças antecipadas | 100% | Contínuo |

---

## 7. Ferramentas de Suporte

### Setup Recomendado

| Ferramenta | Uso | Custo |
|------------|-----|-------|
| **Feedly** | Agregador de feeds | Free |
| **Pocket** | Salvar artigos | Free |
| **Notion** | Base de conhecimento | Free |
| **Google Alerts** | Monitoramento | Free |
| **Similarweb** | Tráfego de concorrentes | Free tier |

### Organização no Notion/Obsidian

```
📁 Research
├── 📁 Insights
│   ├── 2026-01-insights.md
│   └── ...
├── 📁 Competitors
│   ├── omie.md
│   ├── uipath.md
│   └── ...
├── 📁 Market
│   ├── trends.md
│   └── reports.md
└── 📁 Ideas
    └── backlog.md
```

---

## 8. Responsabilidades

### Gabriel (Tech & IA)

| Área | Atividade |
|------|-----------|
| Tecnologia | Monitorar tendências IA/ML |
| Ferramentas | Avaliar novas ferramentas |
| Concorrentes tech | UiPath, Automation Anywhere |
| Comunidades | LangChain, Qdrant, etc. |

### Miguel (Produto & Negócio)

| Área | Atividade |
|------|-----------|
| Mercado | Monitorar PMEs, BPOs |
| Produto | Análise de features |
| Concorrentes BR | Omie, Conta Azul, etc. |
| UX | Tendências de produto |

### Ambos

| Área | Atividade |
|------|-----------|
| Decisões estratégicas | Discussão semanal |
| Oportunidades | Avaliação conjunta |
| Documentação | Manter pasta atualizada |

---

## 9. Calendário Anual

### Q1 2026

| Mês | Foco |
|-----|------|
| Janeiro | Setup de ferramentas, baseline |
| Fevereiro | Análise profunda de concorrentes |
| Março | Validação de oportunidades |

### Q2 2026

| Mês | Foco |
|-----|------|
| Abril | Review de mercado |
| Maio | Análise de tendências |
| Junho | Planejamento S2 |

### Q3 2026

| Mês | Foco |
|-----|------|
| Julho | Análise de novos entrantes |
| Agosto | Review de parcerias |
| Setembro | Preparação para Q4 |

### Q4 2026

| Mês | Foco |
|-----|------|
| Outubro | Tendências para 2027 |
| Novembro | Revisão anual |
| Dezembro | Planejamento 2027 |

---

## 10. Checklist de Setup Inicial

| Item | Status | Responsável | Prazo |
|------|--------|-------------|-------|
| Configurar Google Alerts (5+) | ⬜ | Gabriel | Semana 1 |
| Criar conta Feedly | ⬜ | Miguel | Semana 1 |
| Seguir 20+ perfis LinkedIn | ⬜ | Ambos | Semana 1 |
| Assinar 5 newsletters | ⬜ | Ambos | Semana 1 |
| Criar base no Notion | ⬜ | Miguel | Semana 2 |
| Definir rotina no calendário | ⬜ | Ambos | Semana 2 |
| Primeira análise de concorrentes | ⬜ | Ambos | Semana 3 |
| Primeira revisão de mercado | ⬜ | Ambos | Semana 4 |

---

## 11. Revisão deste Documento

| Frequência | Ação |
|------------|------|
| Mensal | Verificar se rotina está sendo seguida |
| Trimestral | Ajustar fontes e frequências |
| Anual | Revisão completa do plano |

**Próxima revisão**: 2026-02-17

