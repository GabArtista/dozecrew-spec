---
title: Checklist de Governança Documental
status: active
version: 1.0.0
updated: 2026-03-15
owners:
  - Gabriel
  - Miguel
links:
  - /scripts/check_docs_governance.py
  - /00-index/README.md
  - /00-index/decision-log.md
tags:
  - documentation
  - governance
  - quality
  - checklist
---

# Checklist de Governança Documental (SpecKit)

## Objetivo
Garantir consistência, rastreabilidade e manutenção da documentação do repositório em toda mudança de markdown.

## Checklist obrigatório (pré-merge)

- [ ] Todo arquivo `.md` possui frontmatter válido.
- [ ] Campos obrigatórios estão presentes: `status`, `version`, `updated`.
- [ ] `status` usa valores permitidos: `active`, `draft`, `deprecated`, `archived`.
- [ ] `version` segue SemVer (`x.y.z`).
- [ ] `updated` está no formato ISO (`YYYY-MM-DD`).
- [ ] Não há links locais quebrados no frontmatter.
- [ ] Não há links locais quebrados no corpo do markdown.
- [ ] Não há referências legadas proibidas (`/docs/`, `../../spec-project/`).

## Execução automatizada

No diretório raiz do repositório, executar:

```bash
python3 scripts/check_docs_governance.py --root /workspace
```

Critério de aceite:

- Exit code `0` e mensagem: `Resultado: conformidade total de governança documental.`

## Processo recomendado

1. Realizar edição de docs.
2. Rodar checker automatizado.
3. Corrigir não conformidades.
4. Commitar em unidade lógica pequena.
5. Reexecutar checker antes do push final.

## Evoluções futuras

- Integrar checker em CI (GitHub Actions).
- Incluir validação de anchors e convenções de nomenclatura.
- Publicar score de qualidade documental por seção.
