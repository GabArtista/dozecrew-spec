#!/usr/bin/env python3
"""Validador de governança documental para arquivos Markdown.

Regras verificadas:
1) Todo .md deve ter frontmatter YAML.
2) Frontmatter deve conter: status, version, updated.
3) status deve estar em um conjunto permitido.
4) version deve seguir SemVer (x.y.z).
5) updated deve ser data ISO (YYYY-MM-DD).
6) Links locais no frontmatter e no corpo devem resolver.
7) Padrões legados proibidos não devem existir (ex.: /docs/).
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path


REQUIRED_FIELDS = ("status", "version", "updated")
ALLOWED_STATUS = {"active", "draft", "deprecated", "archived"}
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
LEGACY_PATTERNS = ("/docs/", "../../spec-project/")


@dataclass
class Finding:
    file: str
    rule: str
    detail: str


def iter_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for current_root, _, names in os.walk(root):
        parts = Path(current_root).parts
        if ".git" in parts:
            continue
        for name in names:
            if name.endswith(".md"):
                files.append(Path(current_root) / name)
    return sorted(files)


def parse_frontmatter(text: str) -> tuple[list[str] | None, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    end = None
    for idx, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = idx
            break
    if end is None:
        return None, text
    fm_lines = lines[1:end]
    body = "\n".join(lines[end + 1 :])
    return fm_lines, body


def extract_frontmatter_fields(fm_lines: list[str]) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in fm_lines:
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.+?)\s*$", line)
        if m:
            fields[m.group(1)] = m.group(2)
    return fields


def extract_frontmatter_links(fm_lines: list[str]) -> list[str]:
    links: list[str] = []
    in_links = False
    for raw in fm_lines:
        line = raw.rstrip("\n")
        if re.match(r"^links:\s*$", line.strip()):
            in_links = True
            continue
        if in_links:
            # Sai ao encontrar próxima chave de topo.
            if re.match(r"^[A-Za-z0-9_-]+:\s*", line) and not line.startswith("  -"):
                in_links = False
                continue
            item = re.match(r"^\s*-\s*(.+?)\s*$", line)
            if item:
                links.append(item.group(1).strip().strip("\"'"))
    return links


def is_local_link(link: str) -> bool:
    lowered = link.lower()
    if not link:
        return False
    if link.startswith("#"):
        return False
    if lowered.startswith(("http://", "https://", "mailto:")):
        return False
    return True


def resolve_local_link(base_file: Path, link: str, root: Path) -> Path:
    target = link.split("#", 1)[0].strip()
    if target.startswith("/"):
        return (root / target.lstrip("/")).resolve()
    return (base_file.parent / target).resolve()


def has_legacy_pattern(value: str) -> str | None:
    for pattern in LEGACY_PATTERNS:
        if pattern in value:
            return pattern
    return None


def validate_file(path: Path, root: Path) -> list[Finding]:
    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8", errors="ignore")
    rel = str(path.relative_to(root))

    fm_lines, body = parse_frontmatter(text)
    if fm_lines is None:
        findings.append(Finding(rel, "frontmatter", "Frontmatter ausente ou inválido"))
        return findings

    fields = extract_frontmatter_fields(fm_lines)
    for key in REQUIRED_FIELDS:
        if key not in fields:
            findings.append(Finding(rel, "required_field", f"Campo obrigatório ausente: {key}"))

    status = fields.get("status", "").strip().strip("\"'").lower()
    if status and status not in ALLOWED_STATUS:
        allowed = ", ".join(sorted(ALLOWED_STATUS))
        findings.append(Finding(rel, "status_value", f"status inválido '{status}' (permitidos: {allowed})"))

    version = fields.get("version", "").strip().strip("\"'")
    if version and not SEMVER_RE.match(version):
        findings.append(Finding(rel, "version_format", f"version inválido '{version}' (esperado x.y.z)"))

    updated = fields.get("updated", "").strip().strip("\"'")
    if updated:
        if not DATE_RE.match(updated):
            findings.append(Finding(rel, "updated_format", f"updated inválido '{updated}' (esperado YYYY-MM-DD)"))
        else:
            try:
                dt.date.fromisoformat(updated)
            except ValueError:
                findings.append(Finding(rel, "updated_format", f"updated inválido '{updated}' (data inexistente)"))

    # Links no frontmatter (links: [ ... ]).
    for raw_link in extract_frontmatter_links(fm_lines):
        legacy = has_legacy_pattern(raw_link)
        if legacy:
            findings.append(
                Finding(rel, "legacy_pattern", f"Padrão legado em frontmatter link: {legacy}")
            )
        if not is_local_link(raw_link):
            continue
        resolved = resolve_local_link(path, raw_link, root)
        if not resolved.exists():
            findings.append(
                Finding(rel, "frontmatter_link", f"Link local quebrado: {raw_link}")
            )

    # Links no corpo do markdown.
    for match in MD_LINK_RE.finditer(body):
        raw_link = match.group(1).strip()
        legacy = has_legacy_pattern(raw_link)
        if legacy:
            findings.append(Finding(rel, "legacy_pattern", f"Padrão legado em markdown link: {legacy}"))
        if not is_local_link(raw_link):
            continue
        resolved = resolve_local_link(path, raw_link, root)
        if not resolved.exists():
            findings.append(Finding(rel, "markdown_link", f"Link local quebrado: {raw_link}"))

    return findings


def run(root: Path) -> int:
    files = iter_markdown_files(root)
    all_findings: list[Finding] = []
    for md_file in files:
        all_findings.extend(validate_file(md_file, root))

    print(f"Arquivos markdown analisados: {len(files)}")
    print(f"Não conformidades encontradas: {len(all_findings)}")

    if all_findings:
        print("\nDetalhes:")
        for finding in all_findings:
            print(f"- [{finding.rule}] {finding.file}: {finding.detail}")
        return 1

    print("Resultado: conformidade total de governança documental.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Checker de governança documental")
    parser.add_argument(
        "--root",
        default=".",
        help="Diretório raiz do repositório (default: diretório atual)",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()
    return run(root)


if __name__ == "__main__":
    sys.exit(main())
