---
title: Plano de Ação de Riscos - Empresa
status: active
version: 1.0.0
owners:
  - Gabriel
  - Miguel
updated: 2026-01-17
tags:
  - risk
  - strategy
  - enterprise
---

# Plano de Ação de Riscos - Doze Crew

## Contexto

Este documento detalha o plano de ação para mitigar os riscos estratégicos identificados no [risk-register.md](./risk-register.md).

> **Escopo**: Riscos da EMPRESA como um todo, não de projetos específicos.

## Matriz de Priorização

| Prioridade | Critério | Prazo |
|------------|----------|-------|
| **P1** | Impacto crítico no negócio | Imediato |
| **P2** | Impacto moderado | 30 dias |
| **P3** | Impacto baixo/preventivo | 90 dias |

---

## Ações P1 - Imediatas

### A1. Mitigar Dependência de Fundadores

**Risco**: R-001 (Dependência de Fundadores)

| Atributo | Valor |
|----------|-------|
| Owner | Gabriel + Miguel |
| Prazo | 60 dias |
| Status | Em andamento |

**Tarefas**:

- [ ] Documentar processos críticos de cada fundador
- [ ] Criar runbooks para operações essenciais
- [ ] Estabelecer backup cruzado (cada um conhece o trabalho do outro)
- [ ] Definir matriz de decisão quando um estiver ausente

**Critério de Sucesso**: Cada fundador consegue cobrir 80% das funções do outro.

---

### A2. Validar Product-Market Fit

**Risco**: R-002 (PMF Não Validado)

| Atributo | Valor |
|----------|-------|
| Owner | Miguel |
| Prazo | 90 dias |
| Status | Planejado |

**Tarefas**:

- [ ] Conduzir 10+ entrevistas com ICP
- [ ] Rodar experimento de outbound (EXP-001)
- [ ] Medir taxa de conversão diagnóstico → piloto
- [ ] Coletar NPS dos primeiros clientes

**Critério de Sucesso**: Taxa de conversão > 10% e NPS > 40.

---

### A3. Diversificar Pipeline de Vendas

**Risco**: R-003 (Pipeline Concentrado)

| Atributo | Valor |
|----------|-------|
| Owner | Gabriel |
| Prazo | 90 dias |
| Status | Planejado |

**Tarefas**:

- [ ] Lançar canal inbound (SEO/conteúdo)
- [ ] Estabelecer 2+ parcerias de indicação
- [ ] Criar programa de referral com clientes

**Critério de Sucesso**: ≤ 40% do pipeline de um único canal.

---

## Ações P2 - 30 Dias

### A4. Estabelecer Precificação Baseada em Valor

**Risco**: R-004 (Precificação Errada)

| Atributo | Valor |
|----------|-------|
| Owner | Miguel |
| Prazo | 30 dias |
| Status | Planejado |

**Tarefas**:

- [ ] Calcular ROI médio entregue para clientes
- [ ] Benchmark de concorrentes
- [ ] Testar 2-3 faixas de preço
- [ ] Documentar elasticidade de demanda

---

### A5. Implementar Observabilidade de IA

**Risco**: R-005 (Falha de IA em Produção)

| Atributo | Valor |
|----------|-------|
| Owner | Gabriel |
| Prazo | 30 dias |
| Status | Em andamento |

**Tarefas**:

- [ ] Implementar logging de todas as chamadas LLM
- [ ] Criar dashboard de métricas (latência, custo, erros)
- [ ] Definir alertas para anomalias
- [ ] Estabelecer processo de rollback

---

### A6. Formalizar Conformidade LGPD

**Risco**: R-008 (LGPD)

| Atributo | Valor |
|----------|-------|
| Owner | Gabriel |
| Prazo | 30 dias |
| Status | Planejado |

**Tarefas**:

- [ ] Mapear dados pessoais tratados
- [ ] Criar política de privacidade
- [ ] Implementar consentimento e portabilidade
- [ ] Documentar medidas técnicas de proteção

---

## Ações P3 - 90 Dias

### A7. Reduzir Dependência de Fornecedores de IA

**Risco**: R-006 (Dependência OpenAI/Anthropic)

| Atributo | Valor |
|----------|-------|
| Owner | Gabriel |
| Prazo | 90 dias |
| Status | Planejado |

**Tarefas**:

- [ ] Abstrair camada de LLM para multi-provider
- [ ] Testar modelos alternativos (Claude, Llama, Mistral)
- [ ] Documentar fallback procedures

---

### A8. Preparar Escalabilidade

**Risco**: R-012 (Escalabilidade Técnica)

| Atributo | Valor |
|----------|-------|
| Owner | Gabriel |
| Prazo | 90 dias |
| Status | Planejado |

**Tarefas**:

- [ ] Load test da infraestrutura atual
- [ ] Documentar gargalos identificados
- [ ] Criar plano de scaling horizontal
- [ ] Estabelecer métricas de capacidade

---

## Monitoramento

### Revisão Semanal

- Status das ações P1
- Bloqueios e dependências
- Ajustes de prazo se necessário

### Revisão Mensal

- Atualizar risk-register
- Revisar prioridades
- Adicionar novos riscos identificados

---

## Histórico

| Data | Alteração |
|------|-----------|
| 2026-01-17 | Documento criado |

