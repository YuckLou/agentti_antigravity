---
name: prospectar
description: Prospecção B2B no Brasil com o Agentti, sobre a base oficial da Receita Federal. Use quando a pessoa quer achar clientes, saber quais empresas compram o que ela vende, montar uma lista de leads numa cidade, bairro ou raio, ou pede algo como "quem compra X em Y" ou "monte uma lista de empresas".
---

# Prospectar com o Agentti

As ferramentas são as do conector **Agentti** (`buscar_atividade`, `estatisticas_empresas`, `buscar_empresas`,
`listar` (projetos, buscas, geometrias), `projeto`, `salvar_busca`, `criar_geometria`, `salvar_no_projeto`,
`qualificar`, `descobrir_na_web`, `acompanhar_fila`, `listar_leads`, `ver_lead`). Se elas não aparecerem, diga à pessoa para conectar o
Agentti (README do plugin) e pare.

## Projeto primeiro

Tudo o que você fizer tem de aparecer no painel da pessoa, para ela não refazer nada. Antes de buscar:
- `listar` (projetos) e ache o projeto desta oferta e região (pelo nome ou pela `oferta`). Se não houver, crie com
  `projeto` (sem `projeto_id`) **já com a oferta** (`produto`, `publico_alvo`, `proposta_de_valor`, `chamada`). Um projeto por
  oferta e região ("Morango · Vila Mariana"), não um por pedido.
- `listar` (buscas) do projeto: se o recorte já existe, reuse em vez de refazer o raciocínio.
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
   A lista já vem **uma linha por empresa** (filiais juntas) e numa **ordem estável** entre páginas: não confira
   duplicatas item por item. Se o projeto já tem empresas, use `fora_do_projeto` para listar só as novas;
   `removidos` diz quantas filiais e quantas já salvas saíram.
6. **Grave a busca no projeto** (grátis): `salvar_busca` com o recorte mostrado e um nome claro
   ("Confeitarias faixa A · até 2 km da Vila Mariana"). A pessoa abre a mesma lista na Consulta CNPJ do painel;
   dê o link `abrir_no_painel`. Desenhe também a área no mapa do projeto (`criar_geometria`: `cidade` + `uf`,
   com `regiao` se for "X e região", ou `perto_de` + `raio_km`) e dê o `link`, que abre o mapa já nela. Antes,
   veja em `listar` (geometrias) se a área já existe; não duplique.
7. **Salve empresas só quando a pessoa escolher** (`salvar_no_projeto`, 1 de cota por empresa): ela aponta quais,
   ou pede detalhes, exportação, qualificação ou mensagem de empresas que ainda não estão no projeto.
   - Algumas escolhidas na lista: `cnpjs`.
   - "Salve todas" ou "as N melhores": `busca_id` da busca gravada no passo 6 (e `limite`, se for "as N").
     **Nunca pagine `buscar_empresas` para juntar CNPJs.**
   Nas duas formas, a primeira chamada não salva: devolve quantas entram, a cota e um `previa_id`. Mostre isso,
   espere o "sim" e chame de novo com os mesmos parâmetros, `confirmar: true` e o `previa_id`.
   Não salve por conta própria.
8. **Qualifique.** `qualificar` busca site, Instagram, WhatsApp, telefone e e-mail na web, com prova, e guarda o
   que a empresa diz de si (dossiê, skill **pesquisa-profunda**). Explique antes: roda na extensão Agentti do
   Chrome da pessoa, ~30 segundos por empresa, de preferência no **Chrome do Agentti** (atalho em Configurações →
   Extensão Chrome), com a janela atrás das outras e **nunca minimizada**. Como o motor trabalha: skill
   **pesquisa-profunda**, `references/motor.md`. A primeira chamada só
   devolve a prévia (buscas, tempo estimado, cota restante) e um `previa_id`: mostre, espere o "sim" e chame de
   novo com `confirmar: true` e o `previa_id`. Se `extensao_conectada` vier falso, avise que a fila só começa quando ela entrar na extensão.
9. **Acompanhe e entregue.** `acompanhar_fila` (espera até 45 s sozinho; com `andando: true`, chame de novo sem
   comentar no meio); quando terminar, `listar_leads` com `categoria: "qualificados"`.
   Ofereça o próximo passo: rascunhos de abordagem (skill **abordagem**) ou a ficha de uma empresa
   (skill **relatorio-empresa**).
10. **Planilha** das empresas salvas: skill **exportar**, com o mesmo `busca_id`. Todos os formatos pedidos numa
    chamada; o arquivo vem pelo link.
11. **Lista pequena ou sem contato?** Lugares novos ou com nome fantasia diferente podem não aparecer na Receita:
    ofereça a skill **descobrir** (Apple Maps e Google Maps pelo Chrome da pessoa) na mesma área.

## O que a pessoa espera

- **Profundidade, não só contato.** Quem prospecta quer saber quem é a empresa, se está ativa e como abordá-la.
  Depois de qualificar, use o dossiê (`ver_lead` → `o_que_a_empresa_diz`) para dizer isso com fonte. Se ela quer
  conhecer as empresas a fundo (relatório, visita, campanha caprichada), qualifique com `profunda: true`.
- **Relatórios e campanhas do jeito que ela pedir.** Formato (conversa, Word, PDF, planilha), foco, canal, tom e
  quantas empresas seguem o pedido dela. Use as skills **relatorio-empresa**, **relatorio-regiao**, **mercado** e
  **abordagem**; não imponha um modelo quando ela já disse o que quer.

## Local

- Bairro, endereço ou CEP: `perto_de` + `raio_km`. O raio padrão é 3 km; em bairro denso, 1 a 2 km bastam.
  A busca atravessa bairros e municípios vizinhos.
- Cidade inteira: `cidade` + `uf`. Em cidade pequena, prefira a cidade ao raio.
- **"X e região", "arredores", "cidades vizinhas", "grande X": não chute raio.** Chame `regiao` (`tipo:
  "vizinhos"` = a cidade e as que fazem divisa; `"metropolitana"` = a região metropolitana oficial), mostre a
  lista de municípios à pessoa e use `cidade` + `uf` + `regiao` nas buscas, nas estatísticas e em `salvar_busca`.
- Mais de um local: uma chamada por local.

## Regras

- **Dado só vem das ferramentas.** Não invente empresa, contagem, contato nem código.
- **A faixa A/B/C não diz se a empresa compra.** Ela mede o cadastro (porte, tempo ativa, canal, nome fantasia).
  Se a empresa compra ou não é julgamento seu sobre o ramo, e a qualificação traz as provas de contato.
- **Custo sempre com o "sim" da pessoa.** Salvar gasta 1 de descoberta por empresa nova; qualificar gasta 1 por
  empresa buscada. Toda ferramenta que gasta cota responde primeiro com a prévia: mostre quantas e quanto de cota,
  e só chame com `confirmar: true` e o `previa_id` da prévia depois do "sim" dela, **mesmo que o pedido já diga
  "salve" ou "qualifique"**. Sem o `previa_id`, o servidor só repete a prévia; ele vale 10 minutos e uma vez.
  Uma prévia por pedido: não junte várias confirmações numa chamada só.
  Sem custo (todas já no projeto), a ferramenta faz direto.
- **Nada é enviado.** O Agentti não manda mensagem para ninguém.
- **Sócio pessoa física** aparece só pelo primeiro nome, e só quando ajuda a cumprimentar.
- Escreva em português do Brasil, direto, sem jargão de sistema. Chame a pré-qualificação de "faixa" e explique
  na primeira vez.
