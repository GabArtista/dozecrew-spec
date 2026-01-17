---
title: "Core Hub — PRD (Product Requirements Document)"
status: draft
owners:
  - Gabriel
  - Miguel
updated: 2026-01-16
links:
  - /docs/01-company/01-thesis.md
  - /docs/01-company/03-portfolio.md
  - /docs/03-products/core-hub/02-spec.md
  - /docs/03-products/core-hub/03-architecture.md
  - /docs/00-index/decision-log.md
tags:
  - product
  - prd
  - core-hub
  - ia-first
  - backoffice
---

## Contexto

O **Core Hub** é o produto principal da empresa, alinhado à **Tese A** (Copilotos de Operação para Backoffice). É uma plataforma IA-First que automatiza rotinas financeiras/administrativas com trilha auditável, human-in-the-loop e métricas de valor desde o dia 1.

O produto segue a estratégia de **wedge**: começar com 1–2 rotinas de alto ROI antes de expandir.

## Objetivo

Definir o escopo, personas, problemas, soluções, métricas de sucesso e limites do Core Hub para guiar design, engenharia e go-to-market.

## Escopo

- Wedge inicial: **Rotinas Financeiras** (cobrança, conciliação, contas a pagar)
- Plataforma multi-tenant com isolamento de dados
- Human-in-the-loop para ações sensíveis
- Integrações via conectores padronizados
- Observabilidade e auditoria completas

## Não-escopo (v1)

- Rotinas fora do financeiro (RH, compras, etc.) → v2+
- Self-service onboarding (piloto assistido)
- App mobile nativo
- Marketplace de integrações aberto

---

## 1. Problema

### Dor primária (ICP)

**Empresas de 20–200 funcionários** (PMEs, BPOs contábeis, startups em escala) gastam **30–60% do tempo** do backoffice em rotinas repetitivas:

| Rotina | Dor | Impacto |
|--------|-----|---------|
| Cobrança | Envio manual, acompanhamento fragmentado, erros de status | Inadimplência alta, tempo perdido |
| Conciliação bancária | Cruzamento manual, divergências não detectadas | Fechamento atrasado, erros contábeis |
| Contas a pagar | Validação manual de boletos, classificação, aprovação | Pagamentos duplicados, multas |

### Dor secundária

- Falta de **trilha auditável** (quem fez, quando, por quê)
- **Dependência de pessoas-chave** (férias = gargalo)
- **Baixa previsibilidade** de tempo e qualidade

### Alternativas atuais (concorrência indireta)

| Alternativa | Problema |
|-------------|----------|
| Planilhas + e-mail | Erro humano, sem escala, sem auditoria |
| ERPs tradicionais | Caros, rígidos, não automatizam rotinas |
| RPA clássico | Frágil, não lida com exceções, alto custo de manutenção |
| "IA genérica" (chatbots) | Não executa, só responde |

---

## 2. Solução

### Proposta de valor

> **Automatize rotinas financeiras com IA que você entende e controla.**  
> Reduzimos horas de retrabalho e erros — com trilha auditável, aprovação humana e resultado mensurável em 30 dias.

### Wedge inicial [ASSUMPTION: validar com outbound]

| Rotina | Escopo do wedge |
|--------|-----------------|
| **Cobrança automatizada** | Leitura de inadimplência, disparo de cobrança, acompanhamento, escalation |
| **Conciliação bancária** | Cruzamento de extratos × sistema, identificação de divergências, sugestão de ajuste |
| **Contas a pagar** | Validação de boletos, classificação contábil, aprovação em fila |

**Decisão**: Escolher **1 rotina** para o MVP/piloto com base em sinal de canal (outbound). [OPEN]

### Diferenciais

| Diferencial | Descrição |
|-------------|-----------|
| **IA que executa** | Lê documentos, cruza dados, dispara ações (não só responde) |
| **Human-in-the-loop** | Ações sensíveis passam por aprovação antes de executar |
| **Trilha auditável** | Cada ação registrada (o quê, quando, por quê, confiança) |
| **Observabilidade** | Custo, latência, qualidade visíveis por execução |
| **Integrações sem migração** | Conecta a ERPs, planilhas, e-mail, bancos |

---

## 3. Personas

### Persona primária: **Ana, Coordenadora Financeira**

- **Empresa**: PME de serviços, 50 funcionários
- **Time**: 2–3 pessoas no financeiro
- **Dor**: Passa 2–3 dias/semana em cobrança e conciliação manual
- **Motivação**: Reduzir horas e erros, ter mais previsibilidade
- **Objeção**: "A IA vai errar e eu vou ter que consertar"

### Persona secundária: **Carlos, Sócio de BPO Contábil**

- **Empresa**: BPO com 30 clientes
- **Time**: 10 pessoas operacionais
- **Dor**: Rotinas repetitivas não escalam, margem apertada
- **Motivação**: Fazer mais com menos, diferenciar serviço
- **Objeção**: "Meus clientes não vão confiar em IA"

### Anti-persona

- Grandes corporações com compliance rígido e ciclo de compra > 6 meses
- Empresas sem sistema financeiro (só planilhas informais)
- Empresas que não liberam acesso a dados

---

## 4. Funcionalidades (MVP)

### 4.1 Cobrança automatizada (Wedge #1 candidato)

| Funcionalidade | Descrição | Prioridade |
|----------------|-----------|------------|
| Ingestão de inadimplência | Conecta ao ERP/planilha, identifica faturas vencidas | P0 |
| Disparo de cobrança | Envia e-mail/WhatsApp com mensagem padronizada | P0 |
| Aprovação antes de envio | Human-in-the-loop para revisão (opcional por config) | P0 |
| Acompanhamento | Rastreia respostas, atualiza status | P1 |
| Escalation | Notifica responsável se não houver resposta em X dias | P1 |
| Relatório semanal | Horas poupadas, cobranças enviadas, taxa de resposta | P0 |

### 4.2 Conciliação bancária (Wedge #2 candidato)

| Funcionalidade | Descrição | Prioridade |
|----------------|-----------|------------|
| Ingestão de extrato | Conecta ao banco (OFX/CSV) ou leitura manual | P0 |
| Cruzamento | Compara extrato × lançamentos do sistema | P0 |
| Identificação de divergências | Lista itens não conciliados com sugestão | P0 |
| Aprovação de ajuste | Human-in-the-loop para ajustes | P0 |
| Trilha de auditoria | Registro de cada conciliação | P0 |

### 4.3 Contas a pagar (Wedge #3 candidato)

| Funcionalidade | Descrição | Prioridade |
|----------------|-----------|------------|
| Leitura de boleto | OCR/parsing de boleto PDF | P0 |
| Validação | Verifica duplicidade, vencimento, valor | P0 |
| Classificação contábil | Sugere conta com base em histórico | P1 |
| Fila de aprovação | Human-in-the-loop para aprovar pagamentos | P0 |
| Registro em sistema | Lança no ERP após aprovação | P1 |

### 4.4 Plataforma (transversal)

| Funcionalidade | Descrição | Prioridade |
|----------------|-----------|------------|
| Dashboard | Visão de execuções, métricas, filas de aprovação | P0 |
| Configuração de fluxo | Definir regras, limites, canais | P0 |
| Conectores | ERPs (Omie, Conta Azul, SAP B1), planilhas, e-mail, bancos | P0 |
| Human-in-the-loop | Fila de aprovação com contexto e ações | P0 |
| Trilha de auditoria | Log de cada ação (quem, quando, por quê, confiança) | P0 |
| Observabilidade | Custo por execução, latência, qualidade | P1 |
| Multi-tenant | Isolamento de dados por cliente | P0 |
| Autenticação | SSO ou credenciais próprias | P0 |

---

## 5. Integrações (MVP)

### Priorizadas [ASSUMPTION: validar com ICP]

| Sistema | Tipo | Prioridade |
|---------|------|------------|
| Omie | ERP | P0 |
| Conta Azul | ERP | P0 |
| Google Sheets | Planilha | P0 |
| E-mail (SMTP/IMAP) | Comunicação | P0 |
| WhatsApp (API oficial) | Comunicação | P1 |
| Bancos (OFX/CSV) | Financeiro | P0 |

### Limite do piloto

- Até **2 integrações** por piloto (ex.: ERP + e-mail)
- Novas integrações = item de exceção (preço + prazo)

---

## 6. Métricas de sucesso

### Métricas de valor (cliente)

| Métrica | Descrição | Threshold de sucesso |
|---------|-----------|----------------------|
| Horas poupadas/semana | Tempo antes − tempo depois | ≥ 5h/semana |
| Erros evitados | Retrabalho, estornos, multas evitadas | Redução ≥ 30% |
| Tempo de ciclo | Dias para fechar cobrança/conciliação | Redução ≥ 30% |
| SLA de execução | % de rotinas executadas no prazo | ≥ 95% |

### Métricas de custo (interna)

| Métrica | Descrição | Threshold de alerta |
|---------|-----------|---------------------|
| Custo por execução | $ LLM + infra por rotina | ≤ R$ 0,50/execução [OPEN] |
| Custo por cliente/mês | Infra + suporte | ≤ 20% da mensalidade |
| Tempo de onboarding | Dias até primeiro valor | ≤ 14 dias |

### Métricas de qualidade (produto)

| Métrica | Descrição | Threshold |
|---------|-----------|-----------|
| Taxa de aprovação humana | % de ações aprovadas sem edição | ≥ 80% |
| Taxa de rollback | % de ações revertidas | ≤ 5% |
| NPS do piloto | Satisfação do cliente | ≥ 40 |

---

## 7. Limites e pré-requisitos

### Limites (piloto)

| Item | Limite |
|------|--------|
| Integrações | Até 2 |
| Fluxos | 1 fluxo fim-a-fim |
| Volume | X execuções/dia (acordar por piloto) [OPEN] |
| Ambientes | 1 staging + 1 piloto controlado |
| Suporte | Horário comercial, via e-mail/chat |

### Pré-requisitos (cliente)

| Pré-requisito | Descrição |
|---------------|-----------|
| Sponsor | Pessoa com autoridade para aprovar piloto e liberar acessos |
| Acesso a dados | Credenciais ou API do ERP/banco/planilha |
| Processo documentado | Descrição mínima da rotina atual |
| Disponibilidade | 2h/semana para validação durante piloto |

---

## 8. Riscos do produto

| Risco | Mitigação |
|-------|-----------|
| R-001: Escopo infinito | Wedge fechado, limites explícitos, exceções precificadas |
| R-005: Integrações imprevisíveis | Data readiness checklist, conectores padronizados |
| R-006: Falha de qualidade (alucinação) | Guardrails, human-in-the-loop, rollback, testes de regressão |
| R-012: Unit economics invisíveis | Custo por execução medido desde o piloto |

---

## 9. Roadmap (alto nível)

| Fase | Escopo | Timeline |
|------|--------|----------|
| **MVP/Piloto** | 1 wedge + 2 integrações + HIL + auditoria | 4–6 semanas |
| **v1.0** | 2–3 wedges, conectores priorizados, dashboard | 3 meses |
| **v1.5** | Observabilidade avançada, alertas, relatórios | 4–5 meses |
| **v2.0** | Novos domínios (RH, compras), self-service onboarding | 6+ meses |

---

## 10. Decisões

- **Decidido**: Core Hub é o produto principal (Tese A).
- **Decidido**: Wedge inicial = 1 rotina financeira (cobrança OU conciliação OU AP).
- **[OPEN]**: Qual rotina priorizar no MVP (depende de sinal de canal).
- **[OPEN]**: Limite de volume por piloto (execuções/dia).
- **[OPEN]**: Custo-alvo por execução (R$ 0,50 é estimativa).

## Próximos passos

1. Validar wedge com outbound (5–10 conversas).
2. Definir spec funcional detalhado (`02-spec.md`).
3. Definir arquitetura técnica (`03-architecture.md`).
4. Priorizar integrações com base em ICP.


