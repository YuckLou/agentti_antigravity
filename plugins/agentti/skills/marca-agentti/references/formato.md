# Formato do conteúdo (JSON) do gerador

Exemplo completo: [exemplo.json](exemplo.json).

```json
{
  "titulo": "Mercado de <ramo> em <local>",
  "subtitulo": "Estudo de mercado B2B · base da Receita Federal · consulta de DD/MM/AAAA",
  "titulo_curto": "<ramo> · <local>",
  "arquivo": "Agentti - Mercado - <ramo> - <local> - AAAA-MM-DD",
  "data": "DD/MM/AAAA",
  "destaques": [{"valor": "767", "rotulo": "empresas ativas"}],
  "secoes": [{"titulo": "Resumo", "blocos": [ ... ]}],
  "sobre_os_dados": "padrao"
}
```

| Campo | Obrigatório | Observação |
| :--- | :--- | :--- |
| `titulo`, `secoes` | sim | as seções são numeradas sozinhas ("1. Resumo"); `"numerar": false` desliga |
| `titulo_curto` | não | vai no cabeçalho de cada página |
| `arquivo` | não | nome dos arquivos, sem extensão |
| `data` | não | padrão: hoje |
| `destaques` | não | até 4 números grandes no topo |
| `sobre_os_dados` | não | `"padrao"`, `"sem_contatos"` (relatório sem contatos com selo), um texto próprio, ou `false` |

## Blocos (um por objeto, uma chave só)

| Bloco | Forma |
| :--- | :--- |
| texto | `{"texto": "Frase com **negrito**."}` |
| lista | `{"lista": ["item", "**item** com negrito"]}` |
| tabela | `{"tabela": {"colunas": ["A", "B"], "linhas": [["x", "1"]], "legenda": "opcional"}}` |
| gráfico de barras | `{"grafico": {"titulo": "...", "rotulos": ["ME", "EPP"], "valores": [163, 27], "total": 767, "rotulo_categoria": "Porte", "legenda": "..."}}` |
| gráfico empilhado | `{"grafico_empilhado": {"titulo": "...", "categorias": ["ME", "EPP"], "series": {"A": [67, 19], "B": [67, 8], "C": [29, 0]}, "rotulo_categoria": "Porte"}}` |

- `valores` e `series` só com números da ferramenta (sem "%" nem texto). O percentual é calculado sobre `total`
  (sem `total`, sobre a soma).
- Todo gráfico sai com a tabela de números logo abaixo. `"tabela": false` tira a tabela.
- O empilhado mostra cada categoria em 100% com as contagens dentro e o total à direita.
