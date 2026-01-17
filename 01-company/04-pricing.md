---
title: Pricing (Embalagem, Faixas e Regras)
status: draft
owners:
  - Miguel
  - Gabriel
updated: 2026-01-16
links:
  - /docs/01-company/03-portfolio.md
  - /docs/02-ops/05-templates/TPL-003-pilot-sow.md
  - /docs/00-index/decision-log.md
  - /docs/01-company/06-risk-register.md
tags:
  - company
  - pricing
  - packaging
  - go-to-market
---

## Contexto
A empresa inicia com ofertas “wedge” (A1 core e B1 alternativa). Precificação precisa evitar:
- consultoria por hora disfarçada (R-001),
- embalagem confusa (R-008),
- custo variável invisível (R-012).

## Objetivo
Definir modelo de preço inicial (piloto + assinatura), faixas e regras de limites/exceções, com trade-offs explícitos.

## Escopo
- Modelo padrão: setup + mensalidade.
- Faixas iniciais por oferta (A1 e B1).
- Política de limites e cobrança por exceção.
- Política de desconto.

## Não-escopo
- Tabela final “fechada” para todos os segmentos.
- Contratos jurídicos completos.

## Modelo de preço (padrão)
### Componentes
- **Setup (implantação/piloto)**: cobre integração inicial, configuração, instrumentação e entrega do primeiro valor.
- **Mensalidade**: cobre operação, suporte, manutenção, melhoria incremental e custos de infra/LLM dentro de limites.

### Por que não cobrar por hora (trade-off)
- **Pró**: protege escala, força escopo fechado, melhora previsibilidade.
- **Contra**: alguns clientes querem “flexibilidade”; resolve com “exceções” precificadas, não com hora.

## Faixas iniciais (guidelines)
[OPEN] Ajustar com 10 ancoragens de preço e 2 pilotos pagos.

### Oferta A1 — “Copiloto de Rotinas Financeiras”
- **Setup**: R$ 5k–20k
- **Mensalidade**: R$ 2k–10k/mês
- **Quando é piso vs teto (heurística)**:
  - Piso: 1 rotina simples, 1 integração, baixo volume, baixo risco.
  - Teto: 2 rotinas, 2 integrações, volume alto, exigência de auditoria/compliance.

### Oferta B1 — “Conhecimento Vivo + QA”
- **Setup**: R$ 1k–8k
- **Mensalidade**: R$ 1k–6k/mês
- **Heurística**:
  - Piso: base pequena, um canal, baixo volume.
  - Teto: múltiplas fontes/canais, alto volume, governança e relatórios.

## Limites (para proteger entrega e margem)
### Limites padrão (piloto)
- Integrações: até 2 (padrão).
- Escopo: 1 fluxo fim-a-fim (wedge).
- Ambiente: staging + piloto controlado [OPEN].
- Volume: definir faixa (execuções/mensagens) por piloto [OPEN].

### Exceções (cobrança por exceção)
Regras:
- Integração extra = item separado (preço + prazo).
- Volume extra = upgrade de faixa.
- Funcionalidade fora do wedge = novo épico + novo SOW.

## Descontos (política)
### Quando oferecer
- Apenas em troca de algo explícito:
  - case público,
  - indicação,
  - contrato mínimo (ex.: 6 meses),
  - pagamento antecipado.

### Regras
- Desconto exige justificativa e “troca”.
- Evitar desconto “por pressão” (R-013).

## Métricas mínimas por cliente (para unit economics)
- Valor:
  - A1: horas poupadas/semana, erros evitados, SLA/tempo de ciclo.
  - B1: deflexão, TMA, CSAT, taxa de aprovação humana.
- Custo:
  - custo LLM/infra por execução/resposta [OPEN: definir como medir].

## Decisões
- **Decidido**: setup + mensalidade (sem “por hora”).
- **Decidido**: limites e exceções são parte do SOW (TPL-003).
- **[OPEN]**: faixas de volume e a fórmula de “upgrade”.
- **[OPEN]**: critérios de piso/teto por vertical (contabilidade/BPO vs PME vs SaaS).

## Riscos
- R-001, R-008, R-012, R-013 (ver Risk Register).

## Próximos passos
- Rodar 10 conversas de ancoragem de preço (5 para A1, 5 para B1).
- Fechar 2 pilotos pagos com limites explícitos e medir custo variável.
- Ajustar faixas e limites e registrar mudança no Decision Log (sem apagar histórico).



