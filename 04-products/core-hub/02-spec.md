---
title: "Core Hub — Spec Funcional"
status: draft
owners:
  - Gabriel
  - Miguel
updated: 2026-01-16
links:
  - /docs/03-products/core-hub/01-prd.md
  - /docs/03-products/core-hub/03-architecture.md
  - /docs/03-products/core-hub/04-api.md
  - /docs/00-index/decision-log.md
tags:
  - product
  - spec
  - core-hub
  - ia-first
---

## Contexto

Especificação funcional detalhada do Core Hub, traduzindo o PRD em fluxos, regras de negócio, interfaces e critérios de aceite implementáveis.

## Objetivo

Fornecer especificação suficiente para engenharia implementar o MVP com clareza de escopo, limites e comportamento esperado.

## Escopo

- Fluxos de usuário (happy path + edge cases)
- Regras de negócio
- Estados e transições
- Critérios de aceite
- Interfaces (wireframes conceituais)

## Não-escopo

- Design visual final (UI kit)
- Código de implementação
- Infraestrutura (ver `03-architecture.md`)

---

## 1. Fluxos de usuário

### 1.1 Onboarding (piloto assistido)

```
┌─────────────────────────────────────────────────────────────────┐
│  INTAKE → DISCOVERY → SETUP → PILOTO → VALIDAÇÃO               │
└─────────────────────────────────────────────────────────────────┘

1. Intake: cliente preenche formulário, triagem Go/No-Go
2. Discovery: mapeamento de rotina, dados, sistemas (1–3 dias)
3. Setup: configuração de tenant, integrações, fluxo (3–7 dias)
4. Piloto: execução com human-in-the-loop (7–21 dias)
5. Validação: relatório de resultados, decisão de escala
```

**Critérios de aceite (Onboarding):**
- [ ] Tenant criado com isolamento de dados
- [ ] Pelo menos 1 integração configurada e testada
- [ ] Fluxo principal configurado e validado em staging
- [ ] Primeiro valor entregue em ≤ 14 dias

### 1.2 Fluxo: Cobrança automatizada (Wedge #1)

#### Happy path

```
┌─────────────────────────────────────────────────────────────────┐
│  INGESTÃO → ANÁLISE → PREPARAÇÃO → APROVAÇÃO → ENVIO → ACOMP.  │
└─────────────────────────────────────────────────────────────────┘

1. Ingestão: sistema conecta ao ERP, busca faturas vencidas
2. Análise: IA identifica clientes a cobrar, prioriza por valor/dias
3. Preparação: gera mensagem personalizada (template + variáveis)
4. Aprovação (HIL): usuário revisa e aprova/edita/rejeita
5. Envio: dispara cobrança via e-mail ou WhatsApp
6. Acompanhamento: rastreia abertura, resposta, atualiza status
```

#### Estados da cobrança

| Estado | Descrição | Transições permitidas |
|--------|-----------|----------------------|
| `pending_analysis` | Aguardando análise da IA | → `pending_approval` |
| `pending_approval` | Aguardando aprovação humana | → `approved`, `rejected`, `edited` |
| `approved` | Aprovado, aguardando envio | → `sent` |
| `rejected` | Rejeitado pelo usuário | (terminal) |
| `edited` | Editado pelo usuário | → `approved` |
| `sent` | Enviado ao cliente | → `opened`, `responded`, `no_response` |
| `opened` | E-mail aberto (tracking) | → `responded`, `no_response` |
| `responded` | Cliente respondeu | → `resolved`, `escalated` |
| `no_response` | Sem resposta em X dias | → `escalated` |
| `escalated` | Escalado para responsável | → `resolved` |
| `resolved` | Cobrança resolvida (pago/acordo) | (terminal) |

#### Regras de negócio

| Regra | Descrição |
|-------|-----------|
| RN-COB-01 | Só cobrar faturas vencidas há ≥ X dias (configurável, default: 3) |
| RN-COB-02 | Não cobrar mesmo cliente mais de Y vezes/semana (default: 2) |
| RN-COB-03 | Priorizar por valor × dias de atraso (score) |
| RN-COB-04 | Se config `require_approval=true`, toda cobrança passa por HIL |
| RN-COB-05 | Escalation automático se `no_response` após Z dias (default: 7) |
| RN-COB-06 | Não enviar cobrança fora do horário comercial (8h–18h) |

#### Critérios de aceite (Cobrança)

- [ ] Sistema lista faturas vencidas do ERP conectado
- [ ] IA gera mensagem personalizada com dados corretos (nome, valor, vencimento)
- [ ] Usuário pode aprovar, editar ou rejeitar cada cobrança
- [ ] Cobrança aprovada é enviada via canal configurado (e-mail/WhatsApp)
- [ ] Sistema rastreia status e atualiza automaticamente
- [ ] Relatório semanal com: cobranças enviadas, taxa de resposta, valor recuperado

### 1.3 Fluxo: Conciliação bancária (Wedge #2)

#### Happy path

```
┌─────────────────────────────────────────────────────────────────┐
│  INGESTÃO → CRUZAMENTO → DIVERGÊNCIAS → APROVAÇÃO → REGISTRO   │
└─────────────────────────────────────────────────────────────────┘

1. Ingestão: importa extrato (OFX/CSV) ou conecta ao banco
2. Cruzamento: IA compara extrato × lançamentos do sistema
3. Divergências: lista itens não conciliados com sugestão
4. Aprovação (HIL): usuário revisa e aprova/edita ajustes
5. Registro: aplica ajustes no sistema de origem
```

#### Estados da conciliação

| Estado | Descrição | Transições |
|--------|-----------|------------|
| `pending_import` | Aguardando importação de extrato | → `imported` |
| `imported` | Extrato importado | → `analyzing` |
| `analyzing` | IA analisando | → `pending_review` |
| `pending_review` | Aguardando revisão humana | → `approved`, `partial`, `rejected` |
| `approved` | Conciliação aprovada | → `applied` |
| `partial` | Aprovação parcial | → `approved` (após edições) |
| `rejected` | Rejeitada | (terminal ou retry) |
| `applied` | Ajustes aplicados no sistema | (terminal) |

#### Regras de negócio

| Regra | Descrição |
|-------|-----------|
| RN-CONC-01 | Match automático se valor e data coincidem (tolerância: ±R$0,01) |
| RN-CONC-02 | Match por descrição/referência com confiança ≥ 85% |
| RN-CONC-03 | Divergências < threshold (R$50) podem ser auto-aprovadas [OPEN] |
| RN-CONC-04 | Divergências ≥ threshold sempre passam por HIL |
| RN-CONC-05 | Não aplicar ajuste sem aprovação se `require_approval=true` |

#### Critérios de aceite (Conciliação)

- [ ] Sistema importa extrato OFX ou CSV
- [ ] IA identifica matches e divergências
- [ ] Usuário vê lista de divergências com sugestão de ajuste
- [ ] Usuário pode aprovar, editar ou rejeitar cada item
- [ ] Ajustes aprovados são registrados no sistema de origem
- [ ] Trilha de auditoria completa (quem aprovou, quando, por quê)

### 1.4 Fluxo: Contas a pagar (Wedge #3)

#### Happy path

```
┌─────────────────────────────────────────────────────────────────┐
│  LEITURA → VALIDAÇÃO → CLASSIFICAÇÃO → APROVAÇÃO → REGISTRO    │
└─────────────────────────────────────────────────────────────────┘

1. Leitura: OCR/parsing de boleto PDF
2. Validação: verifica duplicidade, vencimento, valor
3. Classificação: sugere conta contábil com base em histórico
4. Aprovação (HIL): usuário revisa e aprova pagamento
5. Registro: lança no ERP para pagamento
```

#### Estados do pagamento

| Estado | Descrição | Transições |
|--------|-----------|------------|
| `pending_read` | Aguardando leitura do boleto | → `read` |
| `read` | Boleto lido | → `validating` |
| `validating` | Validando | → `valid`, `invalid`, `duplicate` |
| `valid` | Válido, aguardando classificação | → `classified` |
| `invalid` | Inválido (erro no boleto) | → manual review |
| `duplicate` | Duplicata detectada | → `rejected` ou override |
| `classified` | Classificado | → `pending_approval` |
| `pending_approval` | Aguardando aprovação | → `approved`, `rejected` |
| `approved` | Aprovado | → `registered` |
| `registered` | Registrado no ERP | (terminal) |

#### Regras de negócio

| Regra | Descrição |
|-------|-----------|
| RN-AP-01 | Detectar duplicidade por: código de barras, valor + cedente + vencimento |
| RN-AP-02 | Alertar se vencimento < 2 dias úteis |
| RN-AP-03 | Classificação sugerida com base em histórico (cedente + valor similar) |
| RN-AP-04 | Pagamentos > R$X sempre passam por aprovação (configurável) |
| RN-AP-05 | Não registrar pagamento sem aprovação se `require_approval=true` |

#### Critérios de aceite (Contas a pagar)

- [ ] Sistema lê boleto PDF e extrai dados (valor, vencimento, cedente, código de barras)
- [ ] Sistema detecta duplicidade
- [ ] IA sugere classificação contábil
- [ ] Usuário pode aprovar, editar classificação ou rejeitar
- [ ] Pagamento aprovado é registrado no ERP
- [ ] Trilha de auditoria completa

---

## 2. Human-in-the-loop (HIL)

### 2.1 Fila de aprovação

**Interface conceitual:**

```
┌─────────────────────────────────────────────────────────────────┐
│  FILA DE APROVAÇÃO                               [3 pendentes]  │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ [Cobrança] Cliente: Empresa XYZ                         │   │
│  │ Valor: R$ 5.000,00 | Vencimento: 10/01/2026 (6 dias)    │   │
│  │ Mensagem: "Prezado, identificamos..."                   │   │
│  │ Confiança: 92%                                          │   │
│  │ [✓ Aprovar] [✎ Editar] [✗ Rejeitar]                    │   │
│  └─────────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ [Conciliação] Divergência: Depósito não identificado    │   │
│  │ Valor: R$ 1.200,00 | Data: 15/01/2026                   │   │
│  │ Sugestão: "Associar a NF 12345"                         │   │
│  │ Confiança: 78%                                          │   │
│  │ [✓ Aprovar] [✎ Editar] [✗ Rejeitar]                    │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Regras de HIL

| Regra | Descrição |
|-------|-----------|
| HIL-01 | Toda ação sensível pode ser configurada como `require_approval=true|false` |
| HIL-02 | Default: aprovação obrigatória para cobrança e pagamentos |
| HIL-03 | Timeout de aprovação: 24h (configurável); após timeout, notifica responsável |
| HIL-04 | Aprovação em lote permitida (máx 10 itens) com revisão individual disponível |
| HIL-05 | Feedback de aprovação alimenta modelo (melhora confiança) |

### 2.3 Níveis de confiança

| Nível | Range | Comportamento |
|-------|-------|---------------|
| Alta | ≥ 90% | Pode auto-aprovar se config permitir |
| Média | 70–89% | Sempre passa por HIL |
| Baixa | < 70% | Destaque visual, revisão obrigatória |

---

## 3. Dashboard

### 3.1 Visão geral

```
┌─────────────────────────────────────────────────────────────────┐
│  DASHBOARD                                    [Jan 2026]        │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐            │
│  │ Execuções    │ │ Aprovações   │ │ Horas        │            │
│  │    127       │ │   89%        │ │   12h        │            │
│  │  esta semana │ │  s/ edição   │ │  poupadas    │            │
│  └──────────────┘ └──────────────┘ └──────────────┘            │
│                                                                 │
│  FILAS                                                          │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ [3] Cobranças pendentes                                 │   │
│  │ [2] Conciliações pendentes                              │   │
│  │ [1] Pagamentos pendentes                                │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  MÉTRICAS (últimos 7 dias)                                     │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Cobranças enviadas: 45 | Taxa resposta: 62%             │   │
│  │ Conciliações: 12 | Divergências: 8 (todas resolvidas)   │   │
│  │ Pagamentos: 23 | Duplicatas evitadas: 2                 │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Relatório semanal (automático)

| Seção | Conteúdo |
|-------|----------|
| Resumo | Execuções, aprovações, horas poupadas |
| Cobrança | Enviadas, respondidas, valor recuperado |
| Conciliação | Processadas, divergências, taxa de match |
| Pagamentos | Processados, duplicatas evitadas |
| Qualidade | Taxa de aprovação, rollbacks, erros |
| Custo | Execuções, custo LLM, custo total |

---

## 4. Configuração de fluxo

### 4.1 Parâmetros configuráveis

| Parâmetro | Descrição | Default |
|-----------|-----------|---------|
| `require_approval` | Aprovação obrigatória | `true` |
| `auto_approve_threshold` | Confiança para auto-aprovar | `90%` |
| `cobranca.dias_minimos` | Dias de atraso mínimo para cobrar | `3` |
| `cobranca.frequencia_maxima` | Máx cobranças/semana por cliente | `2` |
| `cobranca.horario_envio` | Horário permitido para envio | `08:00–18:00` |
| `cobranca.escalation_dias` | Dias sem resposta para escalar | `7` |
| `conciliacao.tolerancia_valor` | Tolerância de match | `R$0,01` |
| `conciliacao.confianca_minima` | Confiança mínima para sugestão | `70%` |
| `pagamento.valor_aprovacao` | Valor mínimo para aprovação obrigatória | `R$0` (todos) |
| `pagamento.alerta_vencimento` | Dias para alertar vencimento próximo | `2` |

### 4.2 Templates de mensagem

```yaml
# Cobrança - Template padrão
cobranca_template:
  subject: "Lembrete de pagamento - Fatura {{ fatura.numero }}"
  body: |
    Prezado(a) {{ cliente.nome }},

    Identificamos que a fatura {{ fatura.numero }} no valor de 
    {{ fatura.valor | currency }} venceu em {{ fatura.vencimento | date }}.

    Para sua comodidade, segue o boleto atualizado em anexo.

    Caso já tenha efetuado o pagamento, desconsidere esta mensagem.

    Atenciosamente,
    {{ empresa.nome }}
```

---

## 5. Trilha de auditoria

### 5.1 Estrutura do log

| Campo | Descrição |
|-------|-----------|
| `id` | UUID do evento |
| `timestamp` | Data/hora UTC |
| `tenant_id` | ID do cliente |
| `user_id` | ID do usuário (ou `system`) |
| `action` | Ação executada |
| `entity_type` | Tipo (cobranca, conciliacao, pagamento) |
| `entity_id` | ID da entidade |
| `input` | Dados de entrada (sanitizados) |
| `output` | Resultado da ação |
| `confidence` | Confiança da IA (se aplicável) |
| `reasoning` | Explicação da IA (se aplicável) |
| `ip_address` | IP do usuário (se aplicável) |

### 5.2 Eventos auditados

| Evento | Descrição |
|--------|-----------|
| `flow.started` | Fluxo iniciado |
| `flow.completed` | Fluxo concluído |
| `flow.failed` | Fluxo falhou |
| `ai.analysis` | IA analisou dados |
| `ai.suggestion` | IA gerou sugestão |
| `hil.pending` | Item enviado para aprovação |
| `hil.approved` | Item aprovado |
| `hil.rejected` | Item rejeitado |
| `hil.edited` | Item editado |
| `action.sent` | Ação enviada (e-mail, WhatsApp) |
| `action.registered` | Ação registrada no sistema |
| `action.rollback` | Ação revertida |
| `config.changed` | Configuração alterada |

---

## 6. Segurança e LGPD

### 6.1 Autenticação e autorização

| Requisito | Implementação |
|-----------|---------------|
| Autenticação | E-mail + senha ou SSO (Google, Microsoft) |
| MFA | Obrigatório para admins, opcional para usuários |
| Sessão | JWT com expiração de 8h, refresh token 7 dias |
| Roles | `admin`, `operator`, `viewer` |

### 6.2 Roles e permissões

| Role | Permissões |
|------|------------|
| `admin` | Configurar fluxos, gerenciar usuários, ver auditoria completa |
| `operator` | Aprovar/rejeitar, ver filas, ver relatórios |
| `viewer` | Apenas visualização de relatórios |

### 6.3 Proteção de dados (LGPD)

| Requisito | Implementação |
|-----------|---------------|
| Minimização | Coletar apenas dados necessários para o fluxo |
| Consentimento | Registro de consentimento no onboarding |
| Acesso | Usuário pode exportar seus dados (DSAR) |
| Exclusão | Usuário pode solicitar exclusão (soft delete + anonimização) |
| Retenção | Logs auditáveis: 5 anos; dados operacionais: configurável |
| Criptografia | Em trânsito (TLS 1.3), em repouso (AES-256) |
| Isolamento | Multi-tenant com isolamento lógico (tenant_id em todas as queries) |

### 6.4 Controle de acesso a dados externos

| Requisito | Implementação |
|-----------|---------------|
| Princípio do menor privilégio | Solicitar apenas permissões necessárias |
| Credenciais | Armazenadas criptografadas (Vault ou similar) |
| Revogação | Usuário pode revogar acesso a qualquer momento |
| Auditoria | Log de todos os acessos a sistemas externos |

---

## 7. Abuso e fraude

### 7.1 Riscos identificados

| Risco | Descrição | Mitigação |
|-------|-----------|-----------|
| Envio massivo | Uso para spam/cobrança indevida | Rate limits, horário comercial, validação de cliente |
| Manipulação de dados | Alterar valores/destinatários | Trilha imutável, checksums, HIL obrigatório |
| Acesso não autorizado | Credenciais comprometidas | MFA, alertas de login suspeito, IP allowlist |
| Exfiltração de dados | Exportação massiva | Rate limits, logs, alertas |

### 7.2 Controles

| Controle | Descrição |
|----------|-----------|
| Rate limiting | Máx X ações/minuto por usuário |
| Anomaly detection | Alertar se volume ou padrão anormal |
| IP allowlist | Opcional, para clientes que exigem |
| Audit log imutável | Append-only, replicado |
| Alerta de fraude | Notificação para admin se comportamento suspeito |

---

## 8. Decisões

- **Decidido**: HIL obrigatório por default para ações sensíveis.
- **Decidido**: Trilha de auditoria imutável com 5 anos de retenção.
- **Decidido**: Roles: admin, operator, viewer.
- **[OPEN]**: Threshold de auto-aprovação para conciliação (R$50?).
- **[OPEN]**: Permitir aprovação em lote (máx 10 itens).

## Próximos passos

1. Validar fluxos com 2–3 usuários do ICP.
2. Definir arquitetura técnica (`03-architecture.md`).
3. Definir API (`04-api.md`).
4. Implementar MVP do wedge escolhido.


