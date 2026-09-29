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

## Seções

Cada seção vira blocos do gerador (entre parênteses):

1. **Resumo** (texto): o tamanho do mercado, onde está, o perfil dominante e a recomendação em uma frase. Os
   quatro números principais vão em `destaques`.
2. **Método** (tabela): ramos e códigos CNAE, local e raio, data da consulta, "contagem completa dos
   estabelecimentos ativos na base da Receita Federal".
3. **Tamanho** (texto): total, empresas distintas, densidade por km² (se houver raio).
4. **Porte** (gráfico): explique o peso do MEI.
5. **Pré-qualificação** (gráfico das faixas + gráfico empilhado porte × faixa): o que a faixa mede e o que não mede.
6. **Maturidade** (gráfico): tempo ativa.
7. **Canais de contato** (gráfico ou tabela): celular, só fixo, sem telefone, e-mail na Receita (ressalva do
   contador).
8. **Onde estão** (gráfico): os 10 bairros ou municípios com mais empresas, e a distância, se houver raio.
9. **Recomendações** (lista): dois ou três recortes, cada um com contagem, motivo e próximo passo.

`sobre_os_dados: "sem_contatos"` (o relatório de região não traz contatos).

## Arquivo

Word e PDF, **sempre pelo gerador da skill marca-agentti** (se ela não carregar pelo nome, leia
`../marca-agentti/SKILL.md`), mesmo que a pessoa tenha pedido só "um PDF". Não use a skill genérica de PDF ou
Word e não escreva código de gráfico. Nome: `Agentti - Mercado - <ramos resumidos> - <local> - <AAAA-MM-DD>`.

Depois de gerar, diga em três linhas o que o relatório conclui e entregue os dois arquivos.

## Regras

- Número só da ferramenta, exato no relatório. Percentuais com uma casa.
- Não transforme contagem em demanda nem capital em faturamento.
- Não invente o mês da base: "base da Receita Federal, atualizada mensalmente".
