---
title: "Core Hub — API Specification"
status: draft
owners:
  - Gabriel
updated: 2026-01-16
links:
  - /docs/03-products/core-hub/02-spec.md
  - /docs/03-products/core-hub/03-architecture.md
  - /docs/03-products/core-hub/05-data.md
  - /docs/00-index/decision-log.md
tags:
  - api
  - core-hub
  - backend
  - rest
---

## Contexto

Especificação da API REST do Core Hub, seguindo OpenAPI 3.1 patterns. A API é o contrato entre frontend, integrações externas e serviços internos.

## Objetivo

Definir endpoints, schemas, autenticação e padrões de resposta para implementação.

## Escopo

- Endpoints de autenticação
- Endpoints de cobrança, conciliação, pagamentos
- Endpoints de aprovação (HIL)
- Endpoints de dashboard e relatórios
- Endpoints de configuração

## Não-escopo

- Webhooks (v1.1+)
- GraphQL (não previsto)

---

## 1. Convenções

### 1.1 Base URL

```
Produção:  https://api.corehub.com.br/v1
Staging:   https://api-staging.corehub.com.br/v1
Local:     http://localhost:8000/v1
```

### 1.2 Autenticação

| Método | Uso |
|--------|-----|
| `Authorization: Bearer <access_token>` | API requests |
| Cookie `refresh_token` (httpOnly) | Renovação de token |
| `X-API-Key: <key>` | Integrações externas (webhooks) |

### 1.3 Headers comuns

```http
Content-Type: application/json
Accept: application/json
X-Request-ID: <uuid>  # Tracing
X-Tenant-ID: <uuid>   # Implícito via JWT
```

### 1.4 Paginação (cursor-based)

```http
GET /v1/cobrancas?limit=20&cursor=eyJpZCI6MTAwfQ==

Response:
{
  "data": [...],
  "pagination": {
    "limit": 20,
    "has_more": true,
    "next_cursor": "eyJpZCI6MTIwfQ=="
  }
}
```

### 1.5 Códigos de resposta

| Código | Uso |
|--------|-----|
| `200` | Sucesso (GET, PUT, PATCH) |
| `201` | Criado (POST) |
| `204` | Sem conteúdo (DELETE) |
| `400` | Bad Request (validação) |
| `401` | Unauthorized (token inválido/expirado) |
| `403` | Forbidden (sem permissão) |
| `404` | Not Found |
| `409` | Conflict (duplicata, estado inválido) |
| `422` | Unprocessable Entity (regra de negócio) |
| `429` | Rate Limit Exceeded |
| `500` | Internal Server Error |

### 1.6 Formato de erro

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dados inválidos",
    "details": [
      {
        "field": "valor",
        "message": "Deve ser maior que zero"
      }
    ],
    "request_id": "abc-123"
  }
}
```

---

## 2. Autenticação

### 2.1 Login

```http
POST /v1/auth/login
Content-Type: application/json

{
  "email": "usuario@empresa.com",
  "password": "********"
}
```

**Response 200:**
```json
{
  "access_token": "eyJ...",
  "token_type": "Bearer",
  "expires_in": 28800,
  "user": {
    "id": "uuid",
    "email": "usuario@empresa.com",
    "name": "João Silva",
    "role": "operator",
    "tenant_id": "uuid"
  }
}
```

**Set-Cookie:** `refresh_token=<token>; HttpOnly; Secure; SameSite=Strict; Max-Age=604800`

### 2.2 Refresh Token

```http
POST /v1/auth/refresh
Cookie: refresh_token=<token>
```

**Response 200:**
```json
{
  "access_token": "eyJ...",
  "token_type": "Bearer",
  "expires_in": 28800
}
```

### 2.3 Logout

```http
POST /v1/auth/logout
Authorization: Bearer <token>
```

**Response 204:** (no content)

### 2.4 Me (usuário atual)

```http
GET /v1/auth/me
Authorization: Bearer <token>
```

**Response 200:**
```json
{
  "id": "uuid",
  "email": "usuario@empresa.com",
  "name": "João Silva",
  "role": "operator",
  "tenant_id": "uuid",
  "permissions": ["cobranca:read", "cobranca:approve", ...]
}
```

---

## 3. Cobrança

### 3.1 Listar cobranças

```http
GET /v1/cobrancas?status=pending_approval&limit=20
Authorization: Bearer <token>
```

**Query params:**

| Param | Tipo | Descrição |
|-------|------|-----------|
| `status` | string | Filtro por status |
| `cliente_id` | uuid | Filtro por cliente |
| `data_inicio` | date | Vencimento a partir de |
| `data_fim` | date | Vencimento até |
| `limit` | int | Itens por página (max 100) |
| `cursor` | string | Cursor de paginação |

**Response 200:**
```json
{
  "data": [
    {
      "id": "uuid",
      "fatura_id": "uuid",
      "cliente": {
        "id": "uuid",
        "nome": "Empresa XYZ",
        "email": "financeiro@xyz.com"
      },
      "valor": 5000.00,
      "vencimento": "2026-01-10",
      "dias_atraso": 6,
      "status": "pending_approval",
      "mensagem_preview": "Prezado, identificamos...",
      "confidence": 0.92,
      "created_at": "2026-01-16T10:00:00Z"
    }
  ],
  "pagination": {
    "limit": 20,
    "has_more": true,
    "next_cursor": "..."
  }
}
```

### 3.2 Obter cobrança

```http
GET /v1/cobrancas/{id}
Authorization: Bearer <token>
```

**Response 200:**
```json
{
  "id": "uuid",
  "fatura_id": "uuid",
  "cliente": {
    "id": "uuid",
    "nome": "Empresa XYZ",
    "email": "financeiro@xyz.com",
    "telefone": "+5511999999999"
  },
  "valor": 5000.00,
  "vencimento": "2026-01-10",
  "dias_atraso": 6,
  "status": "pending_approval",
  "mensagem": {
    "subject": "Lembrete de pagamento - Fatura 12345",
    "body": "Prezado...",
    "canal": "email"
  },
  "confidence": 0.92,
  "reasoning": "Cliente com histórico de pagamento tardio...",
  "historico": [
    {
      "status": "pending_analysis",
      "timestamp": "2026-01-16T09:00:00Z"
    },
    {
      "status": "pending_approval",
      "timestamp": "2026-01-16T10:00:00Z"
    }
  ],
  "created_at": "2026-01-16T09:00:00Z",
  "updated_at": "2026-01-16T10:00:00Z"
}
```

### 3.3 Aprovar cobrança

```http
POST /v1/cobrancas/{id}/approve
Authorization: Bearer <token>
Content-Type: application/json

{
  "comment": "Aprovado, cliente já foi contatado antes"
}
```

**Response 200:**
```json
{
  "id": "uuid",
  "status": "approved",
  "approved_by": "user_id",
  "approved_at": "2026-01-16T10:30:00Z"
}
```

### 3.4 Rejeitar cobrança

```http
POST /v1/cobrancas/{id}/reject
Authorization: Bearer <token>
Content-Type: application/json

{
  "reason": "Cliente já pagou, não identificado no sistema"
}
```

**Response 200:**
```json
{
  "id": "uuid",
  "status": "rejected",
  "rejected_by": "user_id",
  "rejected_at": "2026-01-16T10:30:00Z"
}
```

### 3.5 Editar mensagem

```http
PATCH /v1/cobrancas/{id}/message
Authorization: Bearer <token>
Content-Type: application/json

{
  "subject": "Lembrete atualizado",
  "body": "Texto editado..."
}
```

**Response 200:**
```json
{
  "id": "uuid",
  "status": "edited",
  "mensagem": {
    "subject": "Lembrete atualizado",
    "body": "Texto editado..."
  }
}
```

### 3.6 Aprovar em lote

```http
POST /v1/cobrancas/batch-approve
Authorization: Bearer <token>
Content-Type: application/json

{
  "ids": ["uuid1", "uuid2", "uuid3"],
  "comment": "Aprovação em lote"
}
```

**Response 200:**
```json
{
  "approved": ["uuid1", "uuid2"],
  "failed": [
    {
      "id": "uuid3",
      "error": "Status inválido para aprovação"
    }
  ]
}
```

---

## 4. Conciliação

### 4.1 Iniciar conciliação

```http
POST /v1/conciliacoes
Authorization: Bearer <token>
Content-Type: multipart/form-data

extrato: <arquivo OFX ou CSV>
conta_id: "uuid"
data_referencia: "2026-01"
```

**Response 201:**
```json
{
  "id": "uuid",
  "status": "imported",
  "conta_id": "uuid",
  "data_referencia": "2026-01",
  "total_itens": 150,
  "job_id": "uuid"
}
```

### 4.2 Obter status da conciliação

```http
GET /v1/conciliacoes/{id}
Authorization: Bearer <token>
```

**Response 200:**
```json
{
  "id": "uuid",
  "status": "pending_review",
  "conta_id": "uuid",
  "data_referencia": "2026-01",
  "resumo": {
    "total_itens": 150,
    "conciliados_auto": 142,
    "divergencias": 8
  },
  "created_at": "2026-01-16T10:00:00Z"
}
```

### 4.3 Listar divergências

```http
GET /v1/conciliacoes/{id}/divergencias
Authorization: Bearer <token>
```

**Response 200:**
```json
{
  "data": [
    {
      "id": "uuid",
      "tipo": "nao_identificado",
      "extrato": {
        "data": "2026-01-15",
        "descricao": "DEPOSITO PIX",
        "valor": 1200.00
      },
      "sugestao": {
        "tipo": "associar_nf",
        "nf_id": "uuid",
        "nf_numero": "12345",
        "confidence": 0.78
      },
      "status": "pending_review"
    }
  ],
  "pagination": {...}
}
```

### 4.4 Aprovar divergência

```http
POST /v1/conciliacoes/{id}/divergencias/{divergencia_id}/approve
Authorization: Bearer <token>
Content-Type: application/json

{
  "acao": "associar_nf",
  "nf_id": "uuid"
}
```

**Response 200:**
```json
{
  "id": "uuid",
  "status": "approved",
  "acao_aplicada": "associar_nf"
}
```

---

## 5. Pagamentos (Contas a pagar)

### 5.1 Upload de boleto

```http
POST /v1/pagamentos/upload
Authorization: Bearer <token>
Content-Type: multipart/form-data

boleto: <arquivo PDF>
```

**Response 201:**
```json
{
  "id": "uuid",
  "status": "read",
  "dados_extraidos": {
    "cedente": "Fornecedor ABC",
    "valor": 1500.00,
    "vencimento": "2026-01-20",
    "codigo_barras": "12345...",
    "confidence": 0.95
  },
  "validacoes": {
    "duplicidade": false,
    "vencimento_proximo": true
  }
}
```

### 5.2 Listar pagamentos

```http
GET /v1/pagamentos?status=pending_approval
Authorization: Bearer <token>
```

**Response 200:**
```json
{
  "data": [
    {
      "id": "uuid",
      "cedente": "Fornecedor ABC",
      "valor": 1500.00,
      "vencimento": "2026-01-20",
      "classificacao_sugerida": {
        "conta": "Despesas Operacionais",
        "centro_custo": "TI",
        "confidence": 0.88
      },
      "status": "pending_approval"
    }
  ],
  "pagination": {...}
}
```

### 5.3 Aprovar pagamento

```http
POST /v1/pagamentos/{id}/approve
Authorization: Bearer <token>
Content-Type: application/json

{
  "classificacao": {
    "conta": "Despesas Operacionais",
    "centro_custo": "TI"
  }
}
```

**Response 200:**
```json
{
  "id": "uuid",
  "status": "approved",
  "approved_by": "user_id"
}
```

---

## 6. Aprovações (HIL unificado)

### 6.1 Listar itens pendentes

```http
GET /v1/approvals?tipo=all
Authorization: Bearer <token>
```

**Query params:**

| Param | Tipo | Descrição |
|-------|------|-----------|
| `tipo` | string | `all`, `cobranca`, `conciliacao`, `pagamento` |
| `limit` | int | Itens por página |

**Response 200:**
```json
{
  "data": [
    {
      "id": "uuid",
      "tipo": "cobranca",
      "entidade_id": "uuid",
      "resumo": "Cobrança para Empresa XYZ - R$ 5.000,00",
      "confidence": 0.92,
      "created_at": "2026-01-16T10:00:00Z"
    },
    {
      "id": "uuid",
      "tipo": "conciliacao",
      "entidade_id": "uuid",
      "resumo": "Divergência: depósito R$ 1.200,00",
      "confidence": 0.78,
      "created_at": "2026-01-16T10:05:00Z"
    }
  ],
  "total_pendentes": {
    "cobranca": 3,
    "conciliacao": 2,
    "pagamento": 1
  },
  "pagination": {...}
}
```

---

## 7. Dashboard e relatórios

### 7.1 Métricas do dashboard

```http
GET /v1/dashboard/metrics?periodo=7d
Authorization: Bearer <token>
```

**Query params:**

| Param | Tipo | Descrição |
|-------|------|-----------|
| `periodo` | string | `7d`, `30d`, `mtd`, `custom` |
| `data_inicio` | date | Se custom |
| `data_fim` | date | Se custom |

**Response 200:**
```json
{
  "periodo": {
    "inicio": "2026-01-10",
    "fim": "2026-01-16"
  },
  "execucoes": {
    "total": 127,
    "cobranca": 45,
    "conciliacao": 52,
    "pagamentos": 30
  },
  "aprovacoes": {
    "taxa": 0.89,
    "aprovadas": 113,
    "rejeitadas": 14
  },
  "valor": {
    "cobrancas_enviadas": 125000.00,
    "divergencias_resolvidas": 8500.00,
    "pagamentos_processados": 45000.00
  },
  "horas_poupadas": 12,
  "erros_evitados": 5
}
```

### 7.2 Relatório semanal

```http
GET /v1/reports/weekly?semana=2026-W03
Authorization: Bearer <token>
```

**Response 200:**
```json
{
  "semana": "2026-W03",
  "resumo": {...},
  "cobranca": {...},
  "conciliacao": {...},
  "pagamentos": {...},
  "qualidade": {
    "taxa_aprovacao": 0.89,
    "rollbacks": 2,
    "incidents": 0
  },
  "custo": {
    "execucoes_llm": 450,
    "custo_llm": 12.50,
    "custo_total": 25.00
  }
}
```

---

## 8. Configuração

### 8.1 Obter configuração do tenant

```http
GET /v1/config
Authorization: Bearer <token>
```

**Response 200:**
```json
{
  "tenant_id": "uuid",
  "cobranca": {
    "require_approval": true,
    "auto_approve_threshold": 0.90,
    "dias_minimos_atraso": 3,
    "frequencia_maxima_semana": 2,
    "horario_envio": {"inicio": "08:00", "fim": "18:00"},
    "escalation_dias": 7
  },
  "conciliacao": {
    "require_approval": true,
    "tolerancia_valor": 0.01,
    "confianca_minima": 0.70
  },
  "pagamento": {
    "require_approval": true,
    "valor_aprovacao_obrigatoria": 0,
    "alerta_vencimento_dias": 2
  },
  "integracoes": [
    {
      "id": "uuid",
      "tipo": "erp",
      "provider": "omie",
      "status": "connected"
    }
  ]
}
```

### 8.2 Atualizar configuração

```http
PATCH /v1/config
Authorization: Bearer <token>
Content-Type: application/json

{
  "cobranca": {
    "dias_minimos_atraso": 5
  }
}
```

**Response 200:** (config atualizada)

### 8.3 Conectar integração

```http
POST /v1/integrations
Authorization: Bearer <token>
Content-Type: application/json

{
  "tipo": "erp",
  "provider": "omie",
  "credentials": {
    "app_key": "...",
    "app_secret": "..."
  }
}
```

**Response 201:**
```json
{
  "id": "uuid",
  "tipo": "erp",
  "provider": "omie",
  "status": "connected",
  "created_at": "2026-01-16T10:00:00Z"
}
```

---

## 9. Auditoria

### 9.1 Listar eventos de auditoria

```http
GET /v1/audit?entity_type=cobranca&limit=50
Authorization: Bearer <token>
```

**Query params:**

| Param | Tipo | Descrição |
|-------|------|-----------|
| `entity_type` | string | Filtro por tipo |
| `entity_id` | uuid | Filtro por entidade |
| `action` | string | Filtro por ação |
| `user_id` | uuid | Filtro por usuário |
| `data_inicio` | datetime | A partir de |
| `data_fim` | datetime | Até |

**Response 200:**
```json
{
  "data": [
    {
      "id": "uuid",
      "timestamp": "2026-01-16T10:30:00Z",
      "user_id": "uuid",
      "user_email": "joao@empresa.com",
      "action": "hil.approved",
      "entity_type": "cobranca",
      "entity_id": "uuid",
      "input": {"comment": "Aprovado"},
      "output": {"status": "approved"},
      "confidence": 0.92,
      "ip_address": "192.168.1.100"
    }
  ],
  "pagination": {...}
}
```

---

## 10. Rate Limits

| Endpoint | Limite |
|----------|--------|
| `/v1/auth/*` | 10 req/min por IP |
| `/v1/*` (geral) | 100 req/min por tenant |
| `/v1/*/batch-*` | 10 req/min por tenant |
| Uploads | 20 req/min por tenant |

**Headers de resposta:**
```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1705406400
```

---

## 11. Decisões

- **Decidido**: REST + JSON (não GraphQL).
- **Decidido**: Paginação cursor-based.
- **Decidido**: JWT com refresh token em cookie httpOnly.
- **[OPEN]**: Webhooks para notificações (v1.1+).

## Próximos passos

1. Gerar OpenAPI spec completo (YAML).
2. Implementar endpoints de autenticação.
3. Implementar endpoints de cobrança (wedge #1).
4. Configurar testes de contrato.


