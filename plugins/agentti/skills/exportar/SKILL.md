---
name: exportar
description: Exporta os leads de um projeto do Agentti em CSV, JSON ou Excel, com os contatos achados e o ICP, e entrega o link de download. Use quando a pessoa pede a planilha, a lista, o Excel ou o CSV dos leads, ou quer levar os leads para outro sistema (CRM, planilha).
---

# Exportar leads

1. Ache o projeto com `listar` (projetos) (pelo nome que a pessoa disse). Se houver mais de um parecido, pergunte.
2. **Uma chamada** de `exportar_leads` com o `formato` pedido (sem pedido: `xlsx` para quem vai abrir no Excel,
   `csv` para importar em outro sistema). Pediu mais de um ("planilha e CSV"): `formato: "xlsx"` e
   `tambem_em: ["csv"]`, que devolve um link por formato. O **arquivo do link sai completo** (~45 colunas).
   A resposta traz só uma prévia de 20 linhas (`limite`); `colunas` muda o que vem na prévia.
   Filtros quando a pessoa pedir: `categoria` (ex.: `qualificados`), `faixa_icp`, `com_whatsapp`, `cidade`,
   `bairro`, `busca_id` (só o que veio de uma busca salva) ou `lead_ids` para uma lista escolhida.
3. Entregue:
   - os **links de download**, dizendo que valem **15 minutos**;
   - o total de linhas e as colunas principais;
   - se a pessoa quiser ver na conversa, uma tabela com a prévia.
   Se ela pediu o arquivo **salvo no computador** e você tem terminal, rode os comandos de `baixar` (já vêm com
   o nome do arquivo), na pasta que ela disser. **Nunca monte o arquivo com as linhas da prévia** nem peça mais
   linhas para isso: o link já tem o arquivo inteiro.
4. Se ela quiser a planilha montada aqui (com formatação, abas, gráfico), use uma skill de planilha, se houver, com
   as linhas de `formato: "json"` (aí sim `limite` alto), e não invente coluna que não veio.

## Regras

- Só entram leads **salvos** no projeto. Se a pessoa pedir empresas de uma busca ou de um relatório que ainda não
  foram salvas: ache a busca em `listar` (buscas) e chame `salvar_no_projeto` com o `busca_id` (sem `confirmar`).
  Mostre quantas entram e a cota, espere o "sim", chame de novo com `confirmar: true` e o `previa_id` da prévia,
  e exporte com o mesmo
  `busca_id`. Três chamadas; nunca liste página por página para juntar CNPJs.
- Exportar não gasta cota.
- O arquivo tem dados de contato de empresas: lembre que é para uso comercial da própria pessoa, sem repasse de
  lista.
