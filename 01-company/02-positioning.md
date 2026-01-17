---
title: Posicionamento (Fase 1)
status: draft
owners:
  - Gabriel
  - Miguel
updated: 2026-01-16
links:
  - /docs/01-company/01-thesis.md
  - /docs/00-index/decision-log.md
  - /docs/01-company/06-risk-register.md
tags:
  - company
  - positioning
  - go-to-market
  - ia-first
---

## Contexto
Este documento traduz a tese selecionada em posicionamento, mensagem e prova, com trade-offs explícitos e itens [OPEN].

## Objetivo
Ter um posicionamento nítido para orientar: landing page, outbound, oferta de piloto, e decisões de produto.

## Escopo
- Posicionamento da tese principal (A) e alternativa (B).
- “O que somos / o que não somos”.
- Mensagens, provas, objeções e canais iniciais.

## Não-escopo
- Identidade visual completa.
- Estratégia de conteúdo/SEO de longo prazo.

## Posicionamento — Tese A (principal)

### Categoria e frase de posicionamento
- **Categoria**: automação operacional “IA-First” para backoffice com trilha auditável
- **Posicionamento (1 frase)**:
  - “Automatizamos rotinas críticas do seu backoffice com IA que executa com segurança (human-in-the-loop) e gera trilha auditável — sem trocar seus sistemas.”

### ICP (foco inicial)
- **ICP inicial**: PME 20–200 e/ou BPO/contabilidade com volume e SLA [OPEN]
- **Anti-ICP**:
  - Times sem dono de processo (ninguém responsável por dados e rotina)
  - Operação altamente customizada sem padrões mínimos

### Problema (dor) e urgência
- Alto custo de tempo + erros + retrabalho em rotinas repetitivas
- Baixa previsibilidade (SLA), baixa auditabilidade e dependência de pessoas

### Promessa (outcome) e prova (métrica)
- **Promessa**: reduzir horas/semana e erros; aumentar previsibilidade e auditoria
- **Provas esperadas no piloto**:
  - Horas poupadas/semana
  - Redução de erros/estornos
  - SLA cumprido + logs/auditoria de ações

### Diferenciais (por que nós)
- Integrações + ETL + qualidade de dados (execução real)
- Segurança por design: ações sensíveis com aprovação e níveis de confiança
- Observabilidade: custo, qualidade, explicação e trilha

### O que não somos (limites)
- Não somos “chatbot genérico”
- Não somos “consultoria sem produto” (escopo fechado por wedge)
- Não substituímos ERP; conectamos e automatizamos ao redor

### Objeções previsíveis e resposta
- “Isso vai dar erro e criar risco.”
  - Resposta: human-in-the-loop, trilha auditável, limites de ação, rollback e métricas.
- “Nossa operação é diferente.”
  - Resposta: wedge fechado + integração mínima; exceções viram backlog pago, não escopo gratuito.
- “LGPD/compliance.”
  - Resposta: mínimos privilégios, isolamento por tenant e opção [OPEN] de self-hosted.

### Canais iniciais e trade-offs
- **Canais**: outbound + parcerias com BPO/contabilidade
- **Trade-off**: menos escala no início, mais previsibilidade de receita e feedback.

## Posicionamento — Tese B (alternativa)

### Categoria e frase de posicionamento
- **Categoria**: assistente de suporte/vendas com conhecimento vivo e governança
- **Posicionamento (1 frase)**:
  - “Ajudamos seu time de suporte a responder com consistência e segurança usando conhecimento citável e auditável — medindo deflexão, TMA e qualidade.”

### Diferencial mínimo (para evitar commoditização)
- Governança/qualidade (citações + auditoria + políticas + avaliação contínua)
- WhatsApp PT-BR como canal prioritário [OPEN]

### Canais iniciais e trade-offs
- **Canais**: outbound para Head de CS/Support + parceiros (agências/consultorias CS)
- **Trade-off**: demo rápida, mas competição alta; precisa provar qualidade e ROI.

## Decisões
- **Posicionamento A**: aprovado para teste em outbound (14 dias).
- **Posicionamento B**: aprovado como alternativa para teste em paralelo (14 dias).
- **Itens [OPEN]**:
  - Mercado/região prioritária.
  - Vertical inicial do wedge (A) e stack de canais (B).
  - Política de deployment (SaaS vs self-hosted).

## Riscos
- R-001, R-003, R-005 e R-006 são críticos para o posicionamento da Tese A.
- R-002 é crítico para a Tese B.
Ver `/docs/01-company/06-risk-register.md`.

## Próximos passos
- Converter este posicionamento em 2 landing pages (A e B) + scripts de outbound.
- Definir wedge da Tese A (1–2 rotinas) e escopo do piloto com limites.
- Rodar 14 dias de experimentos com thresholds e registrar resultado no Decision Log.



