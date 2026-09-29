---
name: prospectar
description: Prospecção B2B no Brasil com o Agentti, sobre a base oficial da Receita Federal. Use quando a pessoa quer achar clientes, saber quais empresas compram o que ela vende, montar uma lista de leads numa cidade, bairro ou raio, ou pede algo como "quem compra X em Y" ou "monte uma lista de empresas".
---

# Prospectar com o Agentti

As ferramentas são as do conector **Agentti** (`buscar_atividade`, `estatisticas_empresas`, `buscar_empresas`,
`listar_projetos`, `criar_projeto`, `definir_oferta`, `salvar_busca`, `listar_buscas`, `salvar_no_projeto`,
`qualificar`, `acompanhar_fila`, `listar_leads`, `ver_lead`). Se elas não aparecerem, diga à pessoa para conectar o
Agentti (README do plugin) e pare.

## Projeto primeiro

Tudo o que você fizer tem de aparecer no painel da pessoa, para ela não refazer nada. Antes de buscar:
- `listar_projetos` e ache o projeto desta oferta e região (pelo nome ou pela `oferta`). Se não houver, crie com
  `criar_projeto` **já com a oferta** (`produto`, `publico_alvo`, `proposta_de_valor`, `chamada`). Um projeto por
  oferta e região ("Morango · Vila Mariana"), não um por pedido.
- `listar_buscas` do projeto: se o recorte já existe, reuse em vez de refazer o raciocínio.
- Diga em uma linha em qual projeto está trabalhando.

## Passo a passo

1. **Entenda a oferta.** O que a pessoa vende, onde atende e quem costuma comprar. Se faltar o local, pergunte
   só isso. Não faça questionário. Depois ache ou crie o projeto (acima).
2. **Proponha os ramos compradores.** Pense em todos os ramos que compram o produto, não só no que a pessoa citou.
   Use [references/ramos-compradores.md](references/ramos-compradores.md) como ponto de partida. Mostre a lista em
   dois grupos, **núcleo** (compram com certeza) e **vale testar**, e peça confirmação.
3. **Ache os códigos.** `buscar_atividade` com **todos os ramos numa chamada** (`textos: [...]`). Mostre os
   códigos escolhidos com o nome oficial. Até 15 códigos por busca. Se um ramo não achar, tente o termo formal da
   Receita.
4. **Raio-X antes de listar.** Chame `estatisticas_empresas` com os ramos e o local. Leia o resultado como manda a
   skill **mercado**: tamanho, porte, faixa, canal, distância. Proponha dois ou três recortes com a contagem de cada
   um e deixe a pessoa escolher. Nunca pule este passo: é grátis e evita salvar gente errada.
5. **Liste.** `buscar_empresas` com o recorte escolhido. Mostre uma tabela curta: nome, bairro, distância, porte,
   faixa e o motivo principal (a lista já vem só com isso). No máximo 25 linhas na conversa; o resto fica para as
   próximas páginas. Telefone, e-mail e endereço da Receita só com `detalhe: true`, quando a pessoa pedir.
6. **Grave a busca no projeto** (grátis): `salvar_busca` com o recorte mostrado e um nome claro
   ("Confeitarias faixa A · até 2 km da Vila Mariana"). A pessoa abre a mesma lista na Consulta CNPJ do painel;
   dê o link `abrir_no_painel`.
7. **Salve empresas só quando a pessoa escolher** (`salvar_no_projeto`, 1 de cota por empresa): ela aponta quais,
   ou pede detalhes, exportação, qualificação ou mensagem de empresas que ainda não estão no projeto. Nesses
   casos, diga quantas vão ser salvas e quanto de cota isso gasta, e espere o "sim". Não salve por conta própria.
8. **Qualifique.** `qualificar` busca site, Instagram, WhatsApp, telefone e e-mail na web, com prova. Explique
   antes: roda na extensão Agentti do Chrome da pessoa, uns 20 a 30 segundos por empresa. Mostre a prévia que a
   ferramenta devolve (buscas, tempo estimado, cota restante). Se `extensao_conectada` vier falso, avise que a fila
   só começa quando ela entrar na extensão.
9. **Acompanhe e entregue.** `acompanhar_fila`; quando terminar, `listar_leads` com `categoria: "qualificados"`.
   Ofereça o próximo passo: rascunhos de abordagem (skill **abordagem**) ou a ficha de uma empresa
   (skill **relatorio-empresa**).

## Local

- Bairro, endereço ou CEP: `perto_de` + `raio_km`. O raio padrão é 3 km; em bairro denso, 1 a 2 km bastam.
  A busca atravessa bairros e municípios vizinhos.
- Cidade inteira: `cidade` + `uf`. Em cidade pequena, prefira a cidade ao raio.
- Mais de um local: uma chamada por local.

## Regras

- **Dado só vem das ferramentas.** Não invente empresa, contagem, contato nem código.
- **A faixa A/B/C não diz se a empresa compra.** Ela mede o cadastro (porte, tempo ativa, canal, nome fantasia).
  Se a empresa compra ou não é julgamento seu sobre o ramo, e a qualificação traz as provas de contato.
- **Cota.** Salvar gasta 1 de descoberta por empresa; qualificar gasta 1 por empresa buscada. Sempre confirme
  antes. Acima de 50, diga o número e peça um "sim" explícito.
- **Nada é enviado.** O Agentti não manda mensagem para ninguém.
- **Sócio pessoa física** aparece só pelo primeiro nome, e só quando ajuda a cumprimentar.
- Escreva em português do Brasil, direto, sem jargão de sistema. Chame a pré-qualificação de "faixa" e explique
  na primeira vez.
