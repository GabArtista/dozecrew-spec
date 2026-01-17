---
title: Status do MVP - Empresa
status: active
version: 1.0.0
updated: 2026-01-17
tags:
  - mvp
  - status
  - enterprise
---

# Status do MVP - Doze Crew

## Visão Geral

Status atual do MVP da empresa Doze Crew como um todo.

```
┌─────────────────────────────────────────────────────────────┐
│                    PROGRESSO GERAL                          │
│                                                             │
│  ████████████████░░░░░░░░░░░░░░░░░░░░░░░░  35%             │
│                                                             │
│  Documentação: ██████████████████████████  95%             │
│  Infraestrutura: █████████░░░░░░░░░░░░░░░  30%             │
│  Produto: ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   0%             │
│  Vendas: ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░  10%             │
│  Marketing: ████████░░░░░░░░░░░░░░░░░░░░░  25%             │
└─────────────────────────────────────────────────────────────┘
```

---

## O Que Temos ✅

### Documentação (95%)

| Item | Status | Localização |
|------|--------|-------------|
| Tese e posicionamento | ✅ Completo | `01-company/thesis.md` |
| Portfolio de ofertas | ✅ Completo | `01-company/portfolio.md` |
| Precificação | ✅ Completo | `01-company/pricing.md` |
| GTM | ✅ Completo | `01-company/gtm.md` |
| Processos operacionais | ✅ Completo | `02-operations/` |
| Padrões técnicos | ✅ Completo | `03-standards/` |
| Análise de riscos | ✅ Completo | `05-analysis/` |
| Business Intelligence | ✅ Completo | `06-business-intel/` |
| Specs Core Hub | ✅ Completo | `04-products/core-hub/` |

### Infraestrutura (30%)

| Item | Status | Notas |
|------|--------|-------|
| Servidor K8s | ✅ Configurado | 78.109.16.236 |
| Ingress NGINX | ✅ Funcionando | Let's Encrypt |
| Domínio | ✅ Configurado | tech.dozecrew.com |
| GitHub repos | ✅ Criados | portal, dozecrew-spec |
| CI/CD | ⏳ Pendente | GitHub Actions |
| Monitoramento | ⏳ Pendente | Sentry, logs |

### Marketing (25%)

| Item | Status | Notas |
|------|--------|-------|
| LinkedIn empresa | ✅ Criado | /company/doze-crew |
| Copy do portal | ✅ Definida | spec-project |
| Estratégia SEO | ✅ Documentada | 06-business-intel |
| Blog | ⏳ Pendente | Precisa conteúdo |
| Redes sociais | ⏳ Pendente | Pouco ativo |

### Vendas (10%)

| Item | Status | Notas |
|------|--------|-------|
| ICP definido | ✅ Completo | PMEs 10-100 func |
| Processo de intake | ✅ Documentado | 02-operations |
| Pipeline | ⏳ Vazio | 0 leads ativos |
| Propostas | ⏳ Template | Precisa personalizar |

---

## O Que Falta ❌

### Produto (0%)

| Item | Prioridade | Esforço | Dependência |
|------|------------|---------|-------------|
| Portal institucional | P1 | 2 semanas | Nenhuma |
| Core Hub MVP | P2 | 8 semanas | Portal |
| Copiloto Financeiro | P3 | 6 semanas | Core Hub |

### Infraestrutura

| Item | Prioridade | Esforço | Dependência |
|------|------------|---------|-------------|
| CI/CD pipeline | P1 | 2 dias | Portal pronto |
| Backup automatizado | P2 | 1 dia | DB em prod |
| Alertas e monitoramento | P2 | 2 dias | App em prod |
| CDN Cloudflare | P3 | 1 dia | Domínio |

### Marketing

| Item | Prioridade | Esforço | Dependência |
|------|------------|---------|-------------|
| Portal no ar | P1 | 2 semanas | Código |
| 5 blog posts | P2 | 2 semanas | Portal |
| Perfis LinkedIn ativos | P2 | Contínuo | Conteúdo |
| Material de vendas | P2 | 1 semana | Copy |
| Vídeo institucional | P3 | 2 semanas | Portal |

### Vendas

| Item | Prioridade | Esforço | Dependência |
|------|------------|---------|-------------|
| Primeiro lead | P1 | ? | Portal/Outbound |
| Primeiro diagnóstico | P1 | 1 semana | Lead |
| Primeiro piloto | P1 | 4 semanas | Diagnóstico |
| Primeiro cliente | P1 | 8 semanas | Piloto |

---

## Roadmap para MVP

### Fase 1: Fundação (Semanas 1-2)

| # | Tarefa | Owner | Status |
|---|--------|-------|--------|
| 1 | Finalizar portal | Miguel | ⏳ |
| 2 | Deploy em produção | Gabriel | ⏳ |
| 3 | CI/CD configurado | Gabriel | ⏳ |
| 4 | Domínio ativo | Gabriel | ⏳ |

**Critério de Sucesso**: Portal acessível em tech.dozecrew.com

### Fase 2: Presença (Semanas 3-4)

| # | Tarefa | Owner | Status |
|---|--------|-------|--------|
| 1 | 3 blog posts publicados | Gabriel | ⏳ |
| 2 | LinkedIn ativo (3 posts/semana) | Ambos | ⏳ |
| 3 | Hotjar/GA4 configurados | Gabriel | ⏳ |
| 4 | Formulário de contato testado | Miguel | ⏳ |

**Critério de Sucesso**: 100 visitas no portal

### Fase 3: Validação (Semanas 5-8)

| # | Tarefa | Owner | Status |
|---|--------|-------|--------|
| 1 | 50 outbounds enviados | Gabriel | ⏳ |
| 2 | 5 reuniões agendadas | Ambos | ⏳ |
| 3 | 2 diagnósticos realizados | Ambos | ⏳ |
| 4 | 1 piloto iniciado | Ambos | ⏳ |

**Critério de Sucesso**: 1 piloto pago

---

## Métricas de MVP

### Metas para Considerar "MVP Validado"

| Métrica | Meta | Atual |
|---------|------|-------|
| Portal no ar | Sim | Não |
| Visitas/mês | 500 | 0 |
| Leads/mês | 10 | 0 |
| Diagnósticos | 3 | 0 |
| Pilotos | 1 | 0 |
| MRR | R$ 2.000 | R$ 0 |

### Timeline

```
Jan 2026                                              Mar 2026
  │                                                      │
  ├──────────┬──────────┬──────────┬──────────┬─────────┤
  │  Portal  │ Presença │ Outbound │ Diagnóst │ Piloto  │
  │  (2 sem) │ (2 sem)  │ (2 sem)  │ (2 sem)  │(4 sem)  │
  │          │          │          │          │         │
  └──────────┴──────────┴──────────┴──────────┴─────────┘
```

---

## Bloqueios Atuais

| Bloqueio | Impacto | Solução |
|----------|---------|---------|
| Portal não está no ar | Alto | Priorizar desenvolvimento |
| Sem conteúdo de blog | Médio | Escrever durante dev |
| Sem leads | Alto | Depende do portal |

---

## Próximos Passos Imediatos

1. **Hoje**: Revisar specs do portal
2. **Esta semana**: Iniciar desenvolvimento Laravel
3. **Próxima semana**: Deploy em produção
4. **Em 2 semanas**: Portal no ar

---

## Histórico

| Data | Alteração |
|------|-----------|
| 2026-01-17 | Documento criado |

