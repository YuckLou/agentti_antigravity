---
name: exportar
description: Exporta os leads de um projeto do Agentti em CSV, JSON ou Excel, com os contatos achados e o ICP, e entrega o link de download. Use quando a pessoa pede a planilha, a lista, o Excel ou o CSV dos leads, ou quer levar os leads para outro sistema (CRM, planilha).
---

# Exportar leads

1. Ache o projeto com `listar_projetos` (pelo nome que a pessoa disse). Se houver mais de um parecido, pergunte.
2. `exportar_leads` com o `formato` pedido (sem pedido: `xlsx` para quem vai abrir no Excel, `csv` para importar
   em outro sistema). O **arquivo do link sai completo** (~45 colunas); `colunas` só muda o que volta na conversa
   (`"resumo"` por padrão). Para só olhar o link, `limite: 0`.
   Filtros quando a pessoa pedir: `categoria` (ex.: `qualificados`), `faixa_icp`, `com_whatsapp`, `cidade`,
   `bairro`, `busca_id` (só o que veio de uma busca salva) ou `lead_ids` para uma lista escolhida.
3. Entregue:
   - o **link de download**, dizendo que vale **15 minutos**;
   - o total de linhas e as colunas principais;
   - se a pessoa quiser ver na conversa, uma tabela com até 20 linhas.
4. Se ela quiser a planilha montada aqui (com formatação, abas, gráfico), use uma skill de planilha, se houver, com
   as linhas de `formato: "json"`, e não invente coluna que não veio.

## Regras

- Só entram leads **salvos** no projeto. Se a pessoa pedir empresas de uma busca ou de um relatório que ainda não
  foram salvas: ache a busca em `listar_buscas` e chame `salvar_no_projeto` com o `busca_id` (sem `confirmar`).
  Mostre quantas entram e a cota, espere o "sim", chame de novo com `confirmar: true` e exporte com o mesmo
  `busca_id`. Três chamadas; nunca liste página por página para juntar CNPJs.
- Exportar não gasta cota.
- O arquivo tem dados de contato de empresas: lembre que é para uso comercial da própria pessoa, sem repasse de
  lista.
