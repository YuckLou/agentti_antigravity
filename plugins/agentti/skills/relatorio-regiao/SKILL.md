---
name: relatorio-regiao
description: Relatório de mercado B2B por região em Word e PDF, com os números do Agentti (contagem completa da base da Receita Federal) - tamanho, porte, faixas, tempo ativa, canais, bairros, distância e recomendações, com gráficos e a marca Agentti. Use quando a pessoa pede um PDF, relatório, estudo ou análise de mercado de um ramo numa cidade, bairro ou raio. Para relatório de mercado com dados do Agentti, use esta skill antes da skill genérica de PDF ou Word.
---

# Relatório de região

## Coletar os números

1. Ramos → `buscar_atividade` com todos numa chamada (`textos: [...]`). Confirme a lista de ramos com a pessoa antes de seguir.
2. Local → `perto_de` + `raio_km` ou `cidade` + `uf`.
3. `estatisticas_empresas` com ramos e local: é a base de todo o relatório.
4. Se ajudar a decisão, até três chamadas a mais:
   - por ramo, quando um ramo domina o total;
   - por bairro ou raio menor, para comparar partes da região;
   - com o recorte recomendado (ex.: `porte: "EPP"`, `faixa_minima: "A"`), para dar a contagem exata.
5. Opcional, se a pessoa quiser nomes: `buscar_empresas` com o recorte recomendado, `por_pagina: 10`. Entram só
   nome, bairro, porte e faixa. Sem contatos no relatório de região.
6. **Deixe o estudo no sistema:** ache ou crie o projeto da oferta e região (`listar_projetos` / `criar_projeto`) e
   grave cada recorte recomendado com `salvar_busca` (grátis). Cite no relatório, em "Recomendações", o nome da
   busca salva. Se depois a pessoa pedir os detalhes das empresas, salve as escolhidas no projeto
   (`salvar_no_projeto`, com a cota informada e o "sim" dela) e use a skill **exportar**.

Leia os números como manda a skill **mercado** ([como ler](../mercado/references/como-ler.md)).

## Arquivo: `gerar_relatorio`

Word e PDF saem **da ferramenta `gerar_relatorio`**, no servidor, mesmo que a pessoa tenha pedido só "um PDF".
Não use a skill genérica de PDF ou Word, não escreva código e não digite números: o servidor calcula a
estatística do recorte, os gráficos, as tabelas, o método e a contagem de cada recomendação. **Você escreve a
análise**, que é o que dá valor ao relatório:

- `titulo` e `titulo_curto` ("Confeitarias · Campinas (SP)");
- `busca_id` da busca gravada no passo 6 (ou `recorte` com os mesmos filtros);
- `resumo`: 1 a 3 parágrafos sobre o tamanho, onde está, o perfil e a recomendação, **para a oferta e o pedido
  da pessoa**;
- `analise`: um parágrafo por seção (`porte`, `faixas`, `maturidade`, `canais`, `onde`), o que o número quer
  dizer para quem vende aquele produto (peso do MEI, faixa não é compra, ressalva do e-mail do contador...);
- `recomendacoes`: dois ou três recortes, cada um com `titulo`, `recorte` (só o que muda: `porte`,
  `faixa_minima`, `raio_km`...), `motivo` e `proximo_passo`;
- `secoes_extras`: o que a pessoa pediu e o modelo não tem (sazonalidade, logística, concorrência...), só texto;
- `projeto_id`: o relatório fica guardado no projeto.

Cite no texto só números que vieram das ferramentas. Se voltar `avisos` (número citado que o relatório não
mostra), corrija o texto e gere de novo. Entregue os links do Word e do PDF (valem 15 minutos) e diga em três
linhas o que o relatório conclui. Com `projeto_id`, diga também que o relatório fica no painel, em **Projetos →
Relatórios**.

Link vencido ou "me manda aquele relatório de novo": `listar_relatorios` com o projeto devolve links novos. Não
gere outra vez.

Se `gerar_relatorio` não existir no conector, use o gerador da skill **marca-agentti** (reserva).

## Regras

- Número só da ferramenta, exato no relatório. Percentuais com uma casa.
- Não transforme contagem em demanda nem capital em faturamento.
- Não invente o mês da base: "base da Receita Federal, atualizada mensalmente".
