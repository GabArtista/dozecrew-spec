---
title: Sugestões de Projetos Internos - Empresa
status: active
version: 1.0.0
updated: 2026-01-17
tags:
  - projects
  - internal
  - ideas
  - enterprise
---

# Sugestões de Projetos Internos - Doze Crew

## Contexto

Ideias de projetos internos para a empresa Doze Crew, focados em:
- Utilitários que podem virar produtos
- Ferramentas internas de produtividade
- Automações do próprio negócio
- MVPs para validar mercado

> **Escopo**: Projetos da EMPRESA, não específicos de um cliente.

---

## Matriz de Priorização

| Critério | Peso |
|----------|------|
| **I** - Impacto no negócio | 1-10 |
| **C** - Confiança de execução | 1-10 |
| **E** - Esforço (inverso) | 1-10 |

**ICE Score** = I × C × E / 10

---

## Projetos de Alta Prioridade (ICE > 7)

### 1. Copiloto Financeiro (MVP)

| Atributo | Valor |
|----------|-------|
| **Tipo** | Produto SaaS |
| **ICE** | 8.5 |
| **Prazo** | 8 semanas |
| **Owner** | Gabriel |

**Descrição**: Assistente de IA para análise financeira de PMEs. Upload de planilhas/extratos, perguntas em linguagem natural, insights automáticos.

**Funcionalidades MVP**:
- [ ] Upload de CSV/Excel
- [ ] Parser inteligente de dados financeiros
- [ ] Chat com contexto dos dados
- [ ] 5 relatórios pré-definidos
- [ ] Export PDF

**Potencial**:
- Wedge de entrada para o Core Hub
- Monetização: R$ 99-299/mês
- TAM Brasil: R$ 500M+

**Riscos**:
- Qualidade dos dados de entrada
- Competição com BI tradicional

---

### 2. Base de Conhecimento IA

| Atributo | Valor |
|----------|-------|
| **Tipo** | Produto SaaS |
| **ICE** | 8.0 |
| **Prazo** | 6 semanas |
| **Owner** | Gabriel |

**Descrição**: RAG-as-a-Service para PMEs. Upload de documentos, busca semântica, chat com documentos.

**Funcionalidades MVP**:
- [ ] Upload multi-formato (PDF, DOCX, TXT)
- [ ] Chunking e embedding automático
- [ ] Busca semântica
- [ ] Chat com documentos
- [ ] API para integração

**Potencial**:
- Upsell para clientes de automação
- Monetização: R$ 149-499/mês
- Diferencial: foco em português BR

---

### 3. Gerador de Propostas

| Atributo | Valor |
|----------|-------|
| **Tipo** | Utilitário Interno → Produto |
| **ICE** | 7.5 |
| **Prazo** | 3 semanas |
| **Owner** | Miguel |

**Descrição**: Ferramenta para gerar propostas comerciais automaticamente baseado em templates e dados do cliente.

**Funcionalidades MVP**:
- [ ] Templates de proposta (diagnóstico, piloto, full)
- [ ] Campos dinâmicos (nome, escopo, preço)
- [ ] Geração de PDF branded
- [ ] Histórico de propostas

**Potencial**:
- Usar internamente primeiro
- Depois oferecer para consultorias
- Monetização: R$ 49-99/mês

---

## Projetos de Média Prioridade (ICE 5-7)

### 4. Dashboard de Métricas da Empresa

| Atributo | Valor |
|----------|-------|
| **Tipo** | Utilitário Interno |
| **ICE** | 6.5 |
| **Prazo** | 2 semanas |
| **Owner** | Gabriel |

**Descrição**: Dashboard interno para acompanhar KPIs da empresa (MRR, leads, pipeline, utilização).

**Funcionalidades**:
- [ ] Integração com planilhas/Notion
- [ ] Visualização de KPIs
- [ ] Alertas automáticos
- [ ] Histórico e tendências

---

### 5. Bot de Atendimento WhatsApp

| Atributo | Valor |
|----------|-------|
| **Tipo** | Utilitário → Produto |
| **ICE** | 6.0 |
| **Prazo** | 4 semanas |
| **Owner** | Gabriel |

**Descrição**: Bot de atendimento inicial via WhatsApp com IA para qualificar leads.

**Funcionalidades MVP**:
- [ ] Integração WhatsApp Business API
- [ ] Fluxo de qualificação
- [ ] Agendamento automático
- [ ] Handoff para humano

**Potencial**:
- Usar para própria empresa
- Oferecer para clientes
- Monetização: R$ 199-499/mês

---

### 6. Extrator de Dados de Documentos

| Atributo | Valor |
|----------|-------|
| **Tipo** | Utilitário → Produto |
| **ICE** | 5.5 |
| **Prazo** | 3 semanas |
| **Owner** | Gabriel |

**Descrição**: OCR + IA para extrair dados estruturados de documentos (notas fiscais, contratos, boletos).

**Funcionalidades MVP**:
- [ ] Upload de PDF/imagem
- [ ] OCR com Tesseract/Cloud Vision
- [ ] Extração de campos com LLM
- [ ] Export JSON/CSV
- [ ] API

**Potencial**:
- Integrar no Core Hub
- Standalone para contadores
- Monetização: R$ 0.10-0.50/documento

---

### 7. Automação de Relatórios

| Atributo | Valor |
|----------|-------|
| **Tipo** | Utilitário Interno |
| **ICE** | 5.0 |
| **Prazo** | 2 semanas |
| **Owner** | Miguel |

**Descrição**: Geração automática de relatórios periódicos (semanal, mensal) para clientes e interno.

**Funcionalidades**:
- [ ] Templates de relatório
- [ ] Coleta automática de dados
- [ ] Geração de PDF
- [ ] Envio por email

---

## Projetos de Baixa Prioridade (ICE < 5)

### 8. CLI de Produtividade

| Atributo | Valor |
|----------|-------|
| **Tipo** | Open Source |
| **ICE** | 4.0 |
| **Prazo** | 2 semanas |
| **Owner** | Gabriel |

**Descrição**: CLI com comandos úteis para desenvolvimento (scaffold, deploy, docs).

**Potencial**:
- Marketing via GitHub
- Atrai desenvolvedores
- Posicionamento técnico

---

### 9. Template de Documentação

| Atributo | Valor |
|----------|-------|
| **Tipo** | Open Source |
| **ICE** | 3.5 |
| **Prazo** | 1 semana |
| **Owner** | Miguel |

**Descrição**: Template de documentação estruturada (como este spec-enterprise) para outras empresas.

**Potencial**:
- Marketing via GitHub
- Lead magnet
- Autoridade

---

### 10. Playground de IA

| Atributo | Valor |
|----------|-------|
| **Tipo** | Marketing |
| **ICE** | 3.0 |
| **Prazo** | 3 semanas |
| **Owner** | Gabriel |

**Descrição**: Página interativa no portal para testar funcionalidades de IA (chat, análise de texto, etc).

**Potencial**:
- Atrai visitantes
- Demonstra capacidade
- Captura leads

---

## Ideias em Exploração

| Ideia | Descrição | Próximo Passo |
|-------|-----------|---------------|
| **Monitor de Concorrentes** | Alertas de mudanças em sites/preços | Validar demanda |
| **Gerador de Contratos** | Contratos a partir de templates + IA | Pesquisar mercado |
| **Agregador de Tarefas** | Unificar Notion/Trello/Asana | Avaliar APIs |
| **Transcritor de Reuniões** | Áudio → texto + resumo + action items | Testar Whisper |
| **Calculadora de ROI** | Widget interativo para portal | Definir fórmulas |

---

## Critérios de Seleção

### Para Priorizar

| Critério | Pergunta |
|----------|----------|
| **Dor própria** | Nós mesmos usaríamos? |
| **Validação rápida** | Dá para testar em 2 semanas? |
| **Receita potencial** | Pode gerar receita? |
| **Marketing** | Atrai leads/autoridade? |
| **Sinergia** | Complementa ofertas atuais? |

### Red Flags

| Red Flag | Por quê evitar |
|----------|----------------|
| Muito genérico | Competição demais |
| Muito nicho | Mercado pequeno |
| Muito complexo | Drena recursos |
| Sem diferencial | Por que nós? |

---

## Processo de Ideação

### Weekly Ideation (15min)

1. Cada um traz 1 ideia nova
2. Discutir brevemente
3. Adicionar à lista se promissora
4. Arquivar se não

### Monthly Review (1h)

1. Revisar lista completa
2. Re-calcular ICE
3. Selecionar 1 para próximo mês
4. Definir owner e prazo

---

## Histórico

| Data | Alteração |
|------|-----------|
| 2026-01-17 | Documento criado |

