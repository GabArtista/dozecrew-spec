---
title: "Core Hub — Arquitetura Técnica"
status: draft
owners:
  - Gabriel
updated: 2026-01-16
links:
  - /docs/03-products/core-hub/01-prd.md
  - /docs/03-products/core-hub/02-spec.md
  - /docs/03-products/core-hub/04-api.md
  - /docs/03-products/core-hub/05-data.md
  - /docs/03-products/core-hub/06-llmops.md
  - /docs/00-index/decision-log.md
tags:
  - architecture
  - core-hub
  - ia-first
  - backend
---

## Contexto

Arquitetura técnica do Core Hub, projetada para suportar o MVP (piloto com 1–5 clientes) e escalar para v1 (10–50 clientes) sem refatoração completa.

## Objetivo

Definir componentes, stack tecnológico, padrões de integração, segurança e infraestrutura para implementação do MVP.

## Escopo

- Visão de alto nível (diagrama de componentes)
- Stack tecnológico
- Padrões de comunicação
- Segurança e isolamento
- Infraestrutura e deploy

## Não-escopo

- Código de implementação
- Configuração detalhada de infra (Terraform/Ansible)

---

## 1. Visão geral (Diagrama)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              CORE HUB                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                   │
│  │   Frontend   │────│   API GW     │────│   Backend    │                   │
│  │   (Vue/NG)   │    │   (FastAPI)  │    │   Services   │                   │
│  └──────────────┘    └──────────────┘    └──────────────┘                   │
│         │                   │                   │                            │
│         │                   │                   │                            │
│  ┌──────────────────────────────────────────────────────────────────┐       │
│  │                         MESSAGE QUEUE                             │       │
│  │                      (Redis / RabbitMQ)                           │       │
│  └──────────────────────────────────────────────────────────────────┘       │
│         │                   │                   │                            │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                   │
│  │   Workers    │    │   AI Engine  │    │  Connectors  │                   │
│  │  (Celery)    │    │  (LangChain) │    │   (ETL)      │                   │
│  └──────────────┘    └──────────────┘    └──────────────┘                   │
│         │                   │                   │                            │
│  ┌──────────────────────────────────────────────────────────────────┐       │
│  │                         DATA LAYER                                │       │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐         │       │
│  │  │ Postgres │  │  Redis   │  │  Qdrant  │  │   S3     │         │       │
│  │  │ (main)   │  │ (cache)  │  │ (vector) │  │ (files)  │         │       │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘         │       │
│  └──────────────────────────────────────────────────────────────────┘       │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────┐       │
│  │                     OBSERVABILITY                                 │       │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐         │       │
│  │  │ Grafana  │  │  Loki    │  │  Tempo   │  │  Sentry  │         │       │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘         │       │
│  └──────────────────────────────────────────────────────────────────┘       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
              ┌──────────┐   ┌──────────┐   ┌──────────┐
              │   ERPs   │   │  E-mail  │   │  Bancos  │
              │ (Omie,   │   │  (SMTP/  │   │  (OFX/   │
              │  Conta   │   │   IMAP)  │   │   API)   │
              │  Azul)   │   │          │   │          │
              └──────────┘   └──────────┘   └──────────┘
                           INTEGRAÇÕES EXTERNAS
```

---

## 2. Stack tecnológico

### 2.1 Backend

| Componente | Tecnologia | Justificativa |
|------------|------------|---------------|
| **API Gateway** | FastAPI (Python) | Async, tipado, OpenAPI nativo, ecossistema IA |
| **Workers** | Celery + Redis | Fila robusta, retry, scheduling |
| **AI Engine** | LangChain + LangGraph | Orquestração de agentes, human-in-the-loop nativo |
| **LLM** | OpenAI GPT-4o / Claude (fallback) | Qualidade + custo balanceados |
| **Embeddings** | OpenAI text-embedding-3-small | Custo baixo, qualidade boa |
| **Vector DB** | Qdrant | Self-hosted, performante, filtros |

### 2.2 Frontend

| Componente | Tecnologia | Justificativa |
|------------|------------|---------------|
| **Framework** | Vue 3 ou Angular [OPEN] | Experiência do Miguel |
| **UI Kit** | Tailwind CSS + shadcn/ui | Rápido, customizável |
| **State** | Pinia (Vue) ou NgRx (Angular) | Reatividade, devtools |
| **API Client** | Axios + TanStack Query | Cache, retry, deduplication |

### 2.3 Data

| Componente | Tecnologia | Justificativa |
|------------|------------|---------------|
| **Database** | PostgreSQL 15+ | ACID, JSON, full-text, maduro |
| **Cache** | Redis 7+ | Session, rate limiting, queue |
| **Vector Store** | Qdrant | Embeddings para RAG/busca |
| **File Storage** | S3 / MinIO | Boletos, extratos, anexos |
| **Migrations** | Alembic | Versionamento de schema |

### 2.4 Infraestrutura

| Componente | Tecnologia | Justificativa |
|------------|------------|---------------|
| **Container** | Docker | Consistência, isolamento |
| **Orchestration** | Docker Compose (MVP) → K8s (v1+) | Simplicidade inicial |
| **CI/CD** | GitHub Actions | Integrado, gratuito |
| **Cloud** | AWS / DigitalOcean [OPEN] | Custo-benefício |
| **DNS/CDN** | Cloudflare | DDoS, cache, SSL |

### 2.5 Observabilidade

| Componente | Tecnologia | Justificativa |
|------------|------------|---------------|
| **Metrics** | Prometheus + Grafana | Padrão, open source |
| **Logs** | Loki | Stack unificada |
| **Traces** | Tempo ou Jaeger | Distributed tracing |
| **Errors** | Sentry | Alertas, contexto |
| **LLM Observability** | LangSmith ou custom | Custo, latência, qualidade |

---

## 3. Componentes principais

### 3.1 API Gateway (FastAPI)

**Responsabilidades:**
- Autenticação e autorização (JWT)
- Rate limiting
- Validação de input
- Roteamento para serviços
- OpenAPI docs

**Estrutura:**

```
api/
├── main.py                 # Entrypoint FastAPI
├── config.py               # Settings (Pydantic)
├── dependencies.py         # Injeção de dependências
├── middleware/
│   ├── auth.py             # JWT validation
│   ├── rate_limit.py       # Rate limiting
│   └── tenant.py           # Tenant context
├── routers/
│   ├── auth.py             # Login, refresh
│   ├── cobranca.py         # Endpoints de cobrança
│   ├── conciliacao.py      # Endpoints de conciliação
│   ├── pagamentos.py       # Endpoints de pagamentos
│   ├── approvals.py        # Human-in-the-loop
│   ├── dashboard.py        # Métricas e relatórios
│   └── admin.py            # Config, usuários
└── schemas/
    ├── cobranca.py         # Pydantic models
    ├── conciliacao.py
    └── ...
```

### 3.2 Workers (Celery)

**Responsabilidades:**
- Execução assíncrona de fluxos
- Retry com backoff
- Scheduling (jobs periódicos)
- Processamento de integrações

**Queues:**

| Queue | Prioridade | Uso |
|-------|------------|-----|
| `high` | Alta | HIL approvals, alertas |
| `default` | Normal | Fluxos de cobrança, conciliação |
| `low` | Baixa | Relatórios, jobs de limpeza |
| `integrations` | Normal | Sync com ERPs, bancos |

### 3.3 AI Engine (LangChain/LangGraph)

**Responsabilidades:**
- Orquestração de agentes
- Geração de mensagens
- Análise de documentos
- Classificação e matching
- Human-in-the-loop checkpoints

**Estrutura:**

```
ai/
├── agents/
│   ├── cobranca_agent.py   # Agente de cobrança
│   ├── conciliacao_agent.py
│   └── pagamentos_agent.py
├── chains/
│   ├── message_generator.py
│   ├── document_parser.py
│   └── classifier.py
├── tools/
│   ├── erp_tools.py        # Ferramentas para ERPs
│   ├── email_tools.py
│   └── bank_tools.py
├── prompts/
│   ├── cobranca.yaml
│   ├── conciliacao.yaml
│   └── classificacao.yaml
└── guardrails/
    ├── validators.py       # Validação de output
    └── filters.py          # Filtros de segurança
```

### 3.4 Connectors (Integrações)

**Responsabilidades:**
- Abstração de ERPs/bancos/e-mail
- Normalização de dados
- Retry e circuit breaker
- Credenciais seguras

**Conectores priorizados (MVP):**

| Conector | Tipo | Prioridade |
|----------|------|------------|
| Omie | ERP | P0 |
| Conta Azul | ERP | P0 |
| Google Sheets | Planilha | P0 |
| SMTP/IMAP | E-mail | P0 |
| Bancos (OFX/CSV) | Financeiro | P0 |
| WhatsApp (API oficial) | Comunicação | P1 |

**Interface padrão:**

```python
class BaseConnector(ABC):
    @abstractmethod
    async def authenticate(self, credentials: dict) -> bool: ...
    
    @abstractmethod
    async def fetch(self, resource: str, params: dict) -> list[dict]: ...
    
    @abstractmethod
    async def push(self, resource: str, data: dict) -> dict: ...
    
    @abstractmethod
    async def health_check(self) -> bool: ...
```

---

## 4. Padrões de comunicação

### 4.1 Síncrono (API)

- REST JSON para operações CRUD
- Paginação cursor-based para listas
- Rate limiting: 100 req/min por tenant (ajustável)

### 4.2 Assíncrono (Events)

- Celery tasks para operações longas
- Webhook para notificações externas (opcional)
- Polling ou SSE para atualizações de UI

### 4.3 Padrão de evento

```json
{
  "event_id": "uuid",
  "event_type": "cobranca.approved",
  "timestamp": "2026-01-16T10:30:00Z",
  "tenant_id": "uuid",
  "payload": {
    "cobranca_id": "uuid",
    "approved_by": "user_id",
    "confidence": 0.92
  }
}
```

---

## 5. Multi-tenancy e isolamento

### 5.1 Estratégia

**Escolha: Isolamento lógico (shared database, tenant_id)**

| Opção | Prós | Contras | Decisão |
|-------|------|---------|---------|
| DB por tenant | Isolamento total | Custo alto, complexidade | ❌ |
| Schema por tenant | Bom isolamento | Migrations complexas | ❌ |
| Row-level (tenant_id) | Simples, econômico | Requer disciplina | ✅ MVP |

### 5.2 Implementação

```python
# Middleware de tenant
class TenantMiddleware:
    async def __call__(self, request, call_next):
        tenant_id = get_tenant_from_jwt(request)
        request.state.tenant_id = tenant_id
        return await call_next(request)

# Todas as queries incluem tenant_id
def get_cobranças(db, tenant_id: UUID, filters: dict):
    return db.query(Cobranca).filter(
        Cobranca.tenant_id == tenant_id,
        **filters
    ).all()
```

### 5.3 Isolamento de dados sensíveis

| Dado | Armazenamento | Acesso |
|------|---------------|--------|
| Credenciais de integração | Vault/SecretsManager (criptografado) | Apenas workers |
| Dados de clientes | Postgres (tenant_id) | Apenas tenant owner |
| Logs de auditoria | Append-only, replicado | Admin + tenant owner |
| Arquivos (boletos, extratos) | S3 com prefixo tenant_id | Presigned URLs |

---

## 6. Segurança

### 6.1 Autenticação

| Método | Uso |
|--------|-----|
| JWT (Access Token) | API requests, 8h expiry |
| Refresh Token | Renovação, 7d expiry, httpOnly cookie |
| API Key | Integrações externas (webhooks) |

### 6.2 Autorização

```python
# RBAC com permissões granulares
ROLES = {
    "admin": ["*"],
    "operator": [
        "cobranca:read", "cobranca:approve",
        "conciliacao:read", "conciliacao:approve",
        "pagamentos:read", "pagamentos:approve",
        "dashboard:read"
    ],
    "viewer": [
        "cobranca:read", "conciliacao:read",
        "pagamentos:read", "dashboard:read"
    ]
}
```

### 6.3 Proteções

| Proteção | Implementação |
|----------|---------------|
| SQL Injection | ORM (SQLAlchemy), parameterized queries |
| XSS | CSP headers, sanitização |
| CSRF | SameSite cookies, CSRF token |
| Rate Limiting | Redis-based, por tenant e endpoint |
| Brute Force | Lockout após 5 tentativas |
| Secrets | Vault/SecretsManager, nunca em código |

### 6.4 Criptografia

| Dado | Em trânsito | Em repouso |
|------|-------------|------------|
| API | TLS 1.3 | — |
| Banco | TLS | AES-256 (RDS) |
| Arquivos | TLS | AES-256 (S3 SSE) |
| Credenciais | TLS | AES-256 (Vault) |

---

## 7. Infraestrutura

### 7.1 Ambientes

| Ambiente | Propósito | Infra |
|----------|-----------|-------|
| `local` | Desenvolvimento | Docker Compose |
| `staging` | Testes, QA | Cloud (mínimo) |
| `production` | Clientes | Cloud (escalável) |

### 7.2 MVP (Docker Compose)

```yaml
# docker-compose.yml (simplificado)
services:
  api:
    build: ./api
    ports: ["8000:8000"]
    depends_on: [postgres, redis]
    
  worker:
    build: ./worker
    depends_on: [postgres, redis, qdrant]
    
  frontend:
    build: ./frontend
    ports: ["3000:80"]
    
  postgres:
    image: postgres:15
    volumes: [pgdata:/var/lib/postgresql/data]
    
  redis:
    image: redis:7
    
  qdrant:
    image: qdrant/qdrant
    volumes: [qdrant_data:/qdrant/storage]
    
  minio:
    image: minio/minio
    volumes: [minio_data:/data]
```

### 7.3 Produção (v1+)

| Componente | Serviço | Tamanho inicial |
|------------|---------|-----------------|
| API | ECS / Cloud Run | 2 instâncias |
| Workers | ECS / Cloud Run | 2 instâncias |
| Postgres | RDS / Managed | db.t3.medium |
| Redis | ElastiCache / Managed | cache.t3.micro |
| Qdrant | EC2 / VM | t3.small |
| S3 | S3 / Spaces | — |

### 7.4 CI/CD

```yaml
# .github/workflows/deploy.yml (simplificado)
on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements.txt
      - run: pytest

  deploy-staging:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - run: docker build -t api:${{ github.sha }} .
      - run: docker push $REGISTRY/api:${{ github.sha }}
      - run: deploy-to-staging.sh

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment: production
    steps:
      - run: deploy-to-production.sh
```

---

## 8. Escalabilidade

### 8.1 Gargalos previstos

| Gargalo | Threshold | Mitigação |
|---------|-----------|-----------|
| API | 1000 req/s | Horizontal scaling, cache |
| Workers | 100 jobs/min | Mais workers, priorização |
| Postgres | 10k rows/s | Índices, read replicas |
| LLM | 100 req/min (rate limit) | Queue, fallback, cache |

### 8.2 Estratégias

| Estratégia | Quando |
|------------|--------|
| Cache (Redis) | Dados estáticos, sessões |
| Queue (Celery) | Jobs longos, integrações |
| Read Replicas | Se leitura > 80% |
| Horizontal scaling | Se CPU/mem > 70% |
| LLM caching | Respostas repetitivas |

---

## 9. Decisões

- **Decidido**: FastAPI + Celery + LangChain como stack core.
- **Decidido**: Multi-tenancy via row-level (tenant_id).
- **Decidido**: Docker Compose para MVP, K8s para v1+.
- **[OPEN]**: Frontend em Vue ou Angular (decisão do Miguel).
- **[OPEN]**: Cloud provider (AWS vs DigitalOcean).

## Riscos

- R-005: Integrações imprevisíveis → conectores padronizados, retry, circuit breaker.
- R-012: Unit economics → observabilidade de custo LLM desde o dia 1.

## Próximos passos

1. Definir API spec detalhado (`04-api.md`).
2. Definir data model (`05-data.md`).
3. Implementar scaffold do projeto.
4. Setup de ambiente local com Docker Compose.


