# Agentti para o Google Antigravity

Plugin que ensina o agente do Antigravity a trabalhar com o **Agentti Lead Generator**: prospecção B2B sobre a
base oficial da Receita Federal (todo o Brasil), leitura de mercado, rascunhos de abordagem e relatórios em Word
e PDF.

O conector do Agentti (MCP) entrega os dados. Este plugin entrega o método: que ramos compram o seu produto, como
ler o mercado antes de listar, como escrever uma mensagem que não parece spam e como montar um relatório que o
seu cliente consegue editar.

## O que você precisa

- Uma conta no Agentti: [agentti.ia.br](https://agentti.ia.br).
- Google Antigravity (app, IDE ou CLI `agy`).
- Para relatórios em Word e PDF: Python 3 com `python-docx`, `matplotlib`, `reportlab` e `pymupdf`. Se faltar
  algum, o agente pergunta antes de instalar.
- Para qualificar leads (achar site, Instagram, WhatsApp e e-mail com prova): a extensão Agentti no Chrome.

## Instalar

CLI:

```
agy plugin install https://github.com/YuckLou/agentti_antigravity/plugins/agentti
```

App ou IDE: aba **Customizations** → **Marketplace** → **+** → pela URL acima, ou copie a pasta
`plugins/agentti` para `~/.gemini/config/plugins/agentti`.

Na primeira chamada de uma ferramenta do Agentti, o Antigravity abre o login: entre com a sua conta do Agentti e
autorize. O servidor é `https://app.agentti.ia.br/mcp` (já vem em `mcp_config.json`).

## Comandos

| Comando | O que faz |
| :--- | :--- |
| `/prospectar <o que você vende> em <local>` | do ramo à lista qualificada, passo a passo |
| `/mercado <ramos> em <local>` | quantas empresas existem, de que porte, onde, e os melhores recortes |
| `/abordagem <lead, CNPJ ou projeto>` | rascunhos por canal e a sequência de follow-up |
| `/relatorio-empresa <CNPJ ou lead>` | ficha completa, na conversa ou em Word e PDF |
| `/relatorio-regiao <ramos> em <local>` | relatório de mercado em Word e PDF |
| `/exportar <projeto> [csv, json ou xlsx]` | leads do projeto com link de download (15 min) |

Não precisa decorar: pedir em português normal ("quem compra polpa de fruta na Vila Mariana?") já usa o
caminho certo.

## Privacidade e boas práticas

- O Agentti **não envia mensagens**. Tudo o que o agente escreve é rascunho para você revisar.
- Salvar e qualificar leads consomem a cota do seu plano Agentti; o agente confirma antes.
- Contato comercial entre empresas, uma mensagem por vez, sempre com saída educada. Nada de disparo em massa.
- Este repositório não guarda dado de cliente nem token. Os exemplos usam empresas fictícias.

## Manutenção

As skills vêm do plugin do Claude ([YuckLou/agentti_plugin](https://github.com/YuckLou/agentti_plugin)).
Não edite `plugins/agentti` à mão: mude lá e rode

```
python sincronizar.py
```

O script copia as skills, troca o que é do Claude (`$ARGUMENTS`, `${CLAUDE_PLUGIN_ROOT}`, campos de frontmatter
que o Antigravity não tem) e gera `plugin.json` e `mcp_config.json`. A versão acompanha a do plugin do Claude.
