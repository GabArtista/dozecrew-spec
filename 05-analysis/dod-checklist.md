---
title: Definition of Done - Empresa
status: active
version: 1.0.0
owners:
  - Gabriel
  - Miguel
updated: 2026-01-17
tags:
  - dod
  - quality
  - enterprise
---

# Definition of Done - Doze Crew

## Contexto

Este documento define os critérios padrão de "pronto" para entregas da empresa Doze Crew.

> **Escopo**: DoD para SERVIÇOS e PRODUTOS da empresa, não para projetos específicos.

---

## DoD por Tipo de Entrega

### Diagnóstico

**Prazo**: 5 dias úteis

| # | Critério | Obrigatório |
|---|----------|-------------|
| 1 | Entrevista com stakeholders realizada | ✅ |
| 2 | Mapeamento de processos documentado | ✅ |
| 3 | Dores e oportunidades identificadas | ✅ |
| 4 | Quick wins listados | ✅ |
| 5 | ROI estimado por iniciativa | ✅ |
| 6 | Roadmap sugerido (3-6-12 meses) | ✅ |
| 7 | Apresentação executiva preparada | ✅ |
| 8 | Proposta de piloto anexada | ✅ |

---

### MVP/Piloto

**Prazo**: 4 semanas

| # | Critério | Obrigatório |
|---|----------|-------------|
| 1 | Escopo definido e aprovado | ✅ |
| 2 | Ambiente de teste configurado | ✅ |
| 3 | Funcionalidades core implementadas | ✅ |
| 4 | Testes funcionais passando | ✅ |
| 5 | Documentação de uso criada | ✅ |
| 6 | Treinamento básico realizado | ✅ |
| 7 | Métricas de sucesso definidas | ✅ |
| 8 | Feedback loop estabelecido | ✅ |
| 9 | Plano de rollout documentado | ✅ |
| 10 | Contrato de piloto assinado | ✅ |

---

### Implementação Full

**Prazo**: 8-12 semanas

| # | Critério | Obrigatório |
|---|----------|-------------|
| 1 | Todos os critérios de Piloto | ✅ |
| 2 | Integração com sistemas existentes | ✅ |
| 3 | Migração de dados concluída | ✅ |
| 4 | Testes de integração passando | ✅ |
| 5 | Performance validada | ✅ |
| 6 | Segurança auditada | ✅ |
| 7 | Backup e recovery testados | ✅ |
| 8 | Documentação técnica completa | ✅ |
| 9 | Treinamento da equipe concluído | ✅ |
| 10 | Handover para suporte realizado | ✅ |
| 11 | SLA definido e assinado | ✅ |
| 12 | Go-live aprovado pelo cliente | ✅ |

---

### Produto SaaS (Release)

**Prazo**: Por sprint

| # | Critério | Obrigatório |
|---|----------|-------------|
| 1 | Features do sprint implementadas | ✅ |
| 2 | Testes unitários > 80% cobertura | ✅ |
| 3 | Testes de integração passando | ✅ |
| 4 | Code review aprovado | ✅ |
| 5 | Documentação atualizada | ✅ |
| 6 | Changelog atualizado | ✅ |
| 7 | Deploy em staging validado | ✅ |
| 8 | Smoke tests em produção | ✅ |
| 9 | Monitoramento configurado | ✅ |
| 10 | Rollback testado | ✅ |

---

## DoD por Área

### Código

| # | Critério |
|---|----------|
| 1 | Segue padrões de arquitetura da empresa |
| 2 | Nenhum warning de linter |
| 3 | Documentação inline (docstrings/JSDoc) |
| 4 | Testes unitários para lógica crítica |
| 5 | Sem secrets hardcoded |
| 6 | Logs estruturados implementados |

---

### Documentação

| # | Critério |
|---|----------|
| 1 | README atualizado |
| 2 | API documentada (OpenAPI/Swagger) |
| 3 | Runbook de deploy criado |
| 4 | Troubleshooting guide |
| 5 | Versionamento semântico |

---

### Segurança

| # | Critério |
|---|----------|
| 1 | Inputs validados/sanitizados |
| 2 | Autenticação implementada |
| 3 | Autorização por role |
| 4 | Dados sensíveis criptografados |
| 5 | LGPD compliance verificado |
| 6 | Rate limiting configurado |

---

### Deploy

| # | Critério |
|---|----------|
| 1 | CI/CD pipeline configurado |
| 2 | Ambiente de produção configurado |
| 3 | Secrets via variáveis de ambiente |
| 4 | Health checks implementados |
| 5 | Alertas configurados |
| 6 | Backup automatizado |

---

## Checklist de Revisão

### Antes de Entregar ao Cliente

```markdown
## Revisão Final

- [ ] Todas as funcionalidades testadas
- [ ] Documentação revisada
- [ ] Ambiente limpo e configurado
- [ ] Credenciais de acesso preparadas
- [ ] Apresentação/demo preparada
- [ ] Próximos passos definidos
- [ ] Contrato/proposta atualizado
```

---

### Handover para Suporte

```markdown
## Checklist de Handover

- [ ] Documentação técnica completa
- [ ] Acesso aos ambientes
- [ ] Contatos de escalação definidos
- [ ] SLA documentado
- [ ] Runbook de troubleshooting
- [ ] Histórico de issues conhecido
```

---

## Exceções

### Quando Flexibilizar

| Situação | Flexibilização Permitida |
|----------|--------------------------|
| POC/Spike | Testes podem ser reduzidos |
| Hotfix crítico | Code review post-deploy |
| MVP experimental | Documentação mínima |

### Aprovação de Exceções

- Exceções devem ser documentadas
- Aprovação de ambos fundadores
- Prazo para regularização definido

---

## Histórico

| Data | Alteração |
|------|-----------|
| 2026-01-17 | Documento criado |

