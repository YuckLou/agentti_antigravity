"""Gera o plugin do Antigravity a partir do plugin do Claude (F:\\agentti-plugin\\plugins\\ag).

As skills são as mesmas; o que muda:
- manifesto `plugin.json` (sem `.claude-plugin/`) e MCP em `mcp_config.json` com `serverUrl`;
- o Antigravity não tem `argument-hint`, `user-invocable` nem `$ARGUMENTS`;
- não há `${CLAUDE_PLUGIN_ROOT}`: o gerador de relatório é achado pela pasta da skill;
- roda sempre no computador da pessoa: instalar pacote só com permissão.

Uso: python sincronizar.py [pasta do plugin do Claude]
Toda troca de texto precisa achar o trecho; se o plugin do Claude mudou e o trecho sumiu, o script para.
"""
import json
import re
import shutil
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ORIGEM = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"F:\agentti-plugin\plugins\ag")
DESTINO = AQUI / "plugins" / "agentti"
MCP_URL = "https://app.agentti.ia.br/mcp"
REPO = "YuckLou/agentti_antigravity"

# (arquivo relativo a skills/, trecho do Claude, trecho do Antigravity)
TROCAS = [
    ("exportar/SKILL.md",
     "use a skill de Excel do Claude com as\n   linhas",
     "use uma skill de planilha, se houver, com\n   as linhas"),
    ("marca-agentti/SKILL.md",
     'python "${CLAUDE_PLUGIN_ROOT}/skills/marca-agentti/scripts/gerar_relatorio.py"',
     'python "<pasta desta skill>/scripts/gerar_relatorio.py"'),
    ("marca-agentti/SKILL.md",
     "   Se esse caminho não existir, ache o script com\n"
     "   `find / -name gerar_relatorio.py -path \"*marca-agentti*\" 2>/dev/null | head -1`.",
     "   A pasta desta skill é a deste SKILL.md. Se não souber qual é, o script fica em\n"
     "   `plugins/agentti/skills/marca-agentti/scripts/` dentro de `~/.gemini/config/`, de\n"
     "   `~/.gemini/antigravity-cli/` ou de `.agents/` no projeto."),
    ("marca-agentti/SKILL.md",
     "No ambiente isolado do Claude, instale e rode de novo. No computador da\n"
     "     pessoa (Claude Code), **pergunte antes** de instalar.",
     "O Antigravity roda no computador da pessoa:\n"
     "     **pergunte antes** de instalar (`pip install` com os pacotes que o script listar)."),
]


def trocar(texto: str, antes: str, depois: str, onde: str) -> str:
    if antes not in texto:
        sys.exit(f"Trecho não achado em {onde}: {antes[:60]!r}. Ajuste TROCAS.")
    return texto.replace(antes, depois)


def limpar_skill(texto: str) -> str:
    texto = re.sub(r"^(argument-hint|user-invocable):.*\n", "", texto, flags=re.M)
    texto = re.sub(r"^Pedido recebido pelo comando \(pode vir vazio\): \$ARGUMENTS\n\n", "", texto, flags=re.M)
    return texto


def main():
    manifesto = json.loads((ORIGEM / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    if DESTINO.exists():
        shutil.rmtree(DESTINO)
    shutil.copytree(ORIGEM / "skills", DESTINO / "skills")

    for skill in sorted((DESTINO / "skills").glob("*/SKILL.md")):
        skill.write_text(limpar_skill(skill.read_text(encoding="utf-8")), encoding="utf-8", newline="\n")
    for rel, antes, depois in TROCAS:
        arq = DESTINO / "skills" / rel
        arq.write_text(trocar(arq.read_text(encoding="utf-8"), antes, depois, rel), encoding="utf-8", newline="\n")

    resto = [str(p.relative_to(DESTINO)) for p in (DESTINO / "skills").rglob("*.md")
             if re.search(r"\$ARGUMENTS|CLAUDE_PLUGIN_ROOT|Claude", p.read_text(encoding="utf-8"))]
    if resto:
        sys.exit(f"Ainda cita o Claude: {resto}")

    (DESTINO / "plugin.json").write_text(json.dumps({
        "$schema": "https://antigravity.google/schemas/v1/plugin.json",
        "name": "agentti",
        "displayName": "Agentti",
        "version": manifesto["version"],
        "description": manifesto["description"].replace(" no Claude", ""),
        "logo": f"https://raw.githubusercontent.com/{REPO}/main/plugins/agentti/skills/marca-agentti/assets/logo.png",
        "author": manifesto["author"],
        "homepage": manifesto["homepage"],
        "repository": f"https://github.com/{REPO}",
        "keywords": manifesto["keywords"],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    (DESTINO / "mcp_config.json").write_text(json.dumps(
        {"mcpServers": {"agentti": {"serverUrl": MCP_URL}}}, indent=2) + "\n", encoding="utf-8", newline="\n")

    print(f"plugin agentti {manifesto['version']} gerado em {DESTINO}")


if __name__ == "__main__":
    main()
