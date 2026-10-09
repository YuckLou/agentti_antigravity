---
name: mercado
description: Leitura de mercado B2B com o Agentti (contagem completa da base da Receita Federal). Use quando a pessoa pergunta quantas empresas de um ramo existem num lugar, de que porte são, onde se concentram, se vale a pena atender uma região, ou quer comparar bairros e cidades antes de prospectar.
---

# Mercado: ler a estatística do Agentti

## Passo a passo

1. Ramos → `buscar_atividade` com todos numa chamada (`textos: [...]`). Local → `perto_de` + `raio_km` ou `cidade` + `uf`; "X e região" → `cidade` + `uf` + `regiao` (veja a lista com a ferramenta `regiao`), nunca um raio chutado.
2. `estatisticas_empresas` com os ramos e o local. É **censo** (contagem completa da base), não amostra, e não
   gasta cota.
3. Responda em três blocos, curtos:
   - **Tamanho:** total de estabelecimentos, empresas distintas (matriz e filiais contam uma vez) e, com raio,
     a densidade por km². Com cidade ou região, `contexto` traz a população (IBGE) e os **estabelecimentos por
     10 mil habitantes**, por município: compare entre eles (onde o ramo é mais concentrado, onde há menos oferta)
     e diga o ano do dado. População e PIB per capita descrevem o lugar; **não dizem se a empresa compra**.
   - **Como se divide:** porte, faixa A/B/C, tempo ativa, canal de contato. Uma tabela pequena com números e
     percentuais; nada de repetir o JSON.
   - **Recortes sugeridos:** dois ou três, cada um com a contagem e o motivo. Exemplo: "EPP e Demais, faixa A,
     até 2 km: 84 empresas, as mais estruturadas e perto". Para ter a contagem exata de um recorte, chame a
     estatística de novo com os filtros.
4. Pergunte se a pessoa quer listar um dos recortes (skill **prospectar**, a partir do passo 5). Se houver
   projeto desta oferta e região (`listar_projetos`), ofereça gravar o recorte escolhido com `salvar_busca`
   (grátis), para ele aparecer no painel, e desenhar a área no mapa do projeto com `criar_geometria` (dê o
   `link`, que abre o mapa na área).
5. Se a pessoa quer **ver** onde as empresas estão ("me mostra no mapa", "onde se concentram"), `gerar_imagem_mapa`
   com o mesmo recorte (`calor` para concentração, `pontos` para poucas empresas) e entregue o `link`. Precisa do
   painel aberto no navegador dela; com `precisa_painel`, mostre o link e tente de novo quando ela avisar.

Detalhes de cada campo e das limitações: [references/como-ler.md](references/como-ler.md).

## Comparar locais

Uma chamada por local, com os mesmos ramos e o mesmo raio. Mostre uma tabela com uma coluna por local: total,
densidade, % EPP e Demais, % faixa A, % com celular. Diga qual local parece melhor e por quê, em uma frase.

## Regras

- Diga a origem: "contagem completa da base da Receita Federal".
- Não transforme capital social em faturamento, nem contagem em demanda. A estatística diz quantas empresas
  existem e como é o cadastro delas; não diz quanto compram.
- Não invente o mês da base. Se precisar citar, diga "base da Receita Federal, atualizada mensalmente".
- Números arredondados na conversa (84, 12%), exatos nos relatórios.
