---
name: marca-agentti
description: Gerador dos documentos do Agentti em Word e PDF (cabeçalho com logo, rodapé com a origem dos dados, tabelas e gráficos na marca, seção "Sobre os dados"). Use sempre que for gerar um relatório de empresa ou de região do Agentti como arquivo.
---

# Documentos Agentti: use o gerador

> **Reserva.** O caminho normal é a ferramenta `gerar_relatorio` do conector, que gera no servidor. Use este
> gerador local só se o conector não tiver essa ferramenta.

O visual é fixo no script `scripts/gerar_relatorio.py` desta skill. **Não escreva código de documento nem de
gráfico**: monte o conteúdo em JSON e rode o script. Ele gera o `.docx` (principal, editável) e o `.pdf` do mesmo
conteúdo, com gráficos, cores, logo e rodapé.

1. Monte o JSON no formato de [references/formato.md](references/formato.md) (exemplo em
   [references/exemplo.json](references/exemplo.json)), só com números das ferramentas do Agentti. Grave em
   `conteudo.json`.
2. Rode:
   ```bash
   python "<pasta desta skill>/scripts/gerar_relatorio.py" conteudo.json --saida <pasta> --previa
   ```
   A pasta desta skill é a deste SKILL.md. Se não souber qual é, o script fica em
   `plugins/agentti/skills/marca-agentti/scripts/` dentro de `~/.gemini/config/`, de
   `~/.gemini/antigravity-cli/` ou de `.agents/` no projeto.
3. O script responde uma linha JSON:
   - com `docx` e `pdf`: entregue os dois;
   - com `erro` e `detalhes`: corrija o JSON no ponto indicado e rode de novo;
   - com `instalar`: faltam pacotes. O Antigravity roda no computador da pessoa:
     **pergunte antes** de instalar (`pip install` com os pacotes que o script listar).
4. Conferência: no máximo **uma** olhada na `previa` (a 1ª página, em miniatura). Não renderize as outras páginas.

A marca é discreta e sai inteira ao apagar o cabeçalho, o rodapé e a seção "Sobre os dados". Os estilos
nomeados ("Título Agentti", "Texto Agentti", ...) deixam o cliente trocar o visual de uma vez no Word.
