---
name: relatorio-empresa
description: Ficha completa de uma empresa brasileira pelo Agentti (cadastro da Receita, contatos com prova, porte, rede, localização, sugestão de abordagem e riscos). Use quando a pessoa pede para contar sobre uma empresa, preparar uma visita ou ligação, analisar um CNPJ ou lead, ou quer a ficha em Word ou PDF.
---

# Relatório de empresa

## Achar a empresa

1. Com o id do lead ou o CNPJ: `ver_lead`. Passe o CNPJ **só com os 14 dígitos**, sem ponto, barra ou traço.
   Se a empresa não está salva na conta, a ficha vem só com o cadastro da Receita, sem contatos com prova.
2. Com o CNPJ, `buscar_empresas` com `cnpj` traz a faixa de pré-qualificação e as unidades ativas (se a
   ferramenta ainda não aceitar `cnpj`, procure pelo `nome` com `cidade` + `uf`). O bloco `rede` de `ver_lead`,
   quando vier, traz o mesmo.
3. Empresa fora da conta: pergunte se a pessoa quer salvar num projeto (`salvar_no_projeto`, gasta 1 de cota) e
   qualificar (`qualificar`) para ter os contatos com prova. Sem isso, diga que a ficha é só do cadastro.
4. Só com o nome, sem cidade: pergunte a cidade antes de buscar. Para achar outras unidades do mesmo grupo,
   `buscar_empresas` pelo `nome` fantasia na cidade.

## Seções

1. **Resumo** em três linhas: quem é, tamanho, se vale a abordagem e por qual canal.
2. **Cadastro** (Receita): razão social, nome fantasia, CNPJ, atividade, porte, matriz ou filial, abertura,
   tempo ativa, capital social declarado.
3. **Sócios:** só o primeiro nome de pessoa física e a quantidade. Sócio pessoa jurídica pelo nome da empresa.
4. **Contatos com prova:** um por linha, com o selo (**confirmado** ou **provável**) e de onde veio. O que não foi
   achado aparece como "não encontrado". E-mail da Receita marcado "cadastro da Receita (pode ser do contador)".
5. **Porte e rede:** unidades ativas, matriz, o que isso sugere sobre quem decide a compra.
6. **Onde fica:** endereço, bairro, cidade. Distância, se veio de uma busca por raio.
7. **ICP:** score e classificação (hot ≥ 60, warm ≥ 30), com o detalhe que a ficha trouxer.
8. **Sugestão de abordagem:** canal, gancho e pedido, seguindo a skill **abordagem**. Um rascunho curto.
9. **Riscos e lacunas:** o que falta provar, empresa nova, só fixo, e-mail do contador, sem site.
10. **Sobre os dados** (só no arquivo): ver a skill **marca-agentti**.

## Formato

- **Na conversa:** texto com as seções acima, sem a 10.
- **Como arquivo** (quando a pessoa pedir Word, PDF, "arquivo" ou "para imprimir"): `gerar_relatorio` com
  `tipo: "empresa"`, `cnpj`, `titulo` (o nome fantasia), `resumo` e `analise` com `rede`, `abordagem` e
  `riscos` (um por linha). Cadastro, sócios, contatos com prova, rede e endereço saem do servidor; não digite
  esses dados. `projeto_id` guarda a ficha no projeto (painel: **Projetos → Relatórios**; link vencido:
  `listar_relatorios`). Entregue os links (15 minutos). Não use a skill genérica
  de PDF ou Word. Se `gerar_relatorio` não existir no conector, use o gerador da skill **marca-agentti**.

## Regras

- Tudo da ficha sai de `ver_lead` ou `buscar_empresas`. O que não veio de lá não entra, nem como suposição.
- Não pesquise a empresa em outros sites para completar a ficha: o Agentti já faz a busca na web com prova,
  pela qualificação.
- Diga a origem de cada bloco: "cadastro da Receita", "qualificação do Agentti em <data>".
