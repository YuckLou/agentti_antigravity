# Como o motor do Agentti trabalha

Use para explicar à pessoa de onde vem cada dado, por que algo não foi achado e quanto tempo leva.

## Três camadas

| Camada | O que faz | Custo | Onde roda |
|---|---|---|---|
| **Pré-qualificação** (faixa A/B/C) | Nota do cadastro da Receita: porte, tempo ativa, canal de contato, nome fantasia | grátis | servidor |
| **Qualificação** (`qualificar`) | Acha e prova site, Instagram, WhatsApp, telefone e e-mail; guarda o dossiê | 1 de cota por empresa | Chrome da pessoa |
| **Descoberta** (`descobrir_na_web`) | Acha no Google Maps lugares que a Receita não mostra ou mostra sem contato | 1 de cota por empresa nova | Chrome da pessoa |

## A qualificação, passo a passo

1. **Busca de texto** pelo nome e a cidade. No Chrome do Agentti, no Yahoo Brasil ou no Ecosia (revezando), numa
   janela própria; fora dele, no Google (lê também a resposta de IA do Google).
2. **Ficha do Google Maps:** telefone e site. Endereço igual ao da Receita = confirmado. No Chrome do Agentti ela
   abre junto com a busca de texto, e o site e o Instagram mais prováveis já abrem nas suas janelas.
3. **Site:** visita até 2 candidatos. Prova é o CNPJ, o telefone ou o endereço da Receita na página. Site fora
   do ar é descartado.
4. **Instagram:** visita o melhor perfil (e o segundo, se empatar). Prova é o endereço ou o site da empresa no
   perfil. Abre também a página do link da bio (Linktree e parecidas) atrás de WhatsApp.
5. **Bing**, só quando a busca foi no Google e nem ela nem o Maps trouxeram site ou telefone.
6. **Selo:** **confirmado** = a página traz o endereço ou o telefone da Receita; **provável** = indícios fortes
   sem essa prova. O resto fica de fora.
7. **Dossiê:** das páginas aceitas, guarda o que a empresa diz de si (bio, legendas com data, avaliações, texto do
   site e, a fundo, das páginas internas). Aparece em `ver_lead` → `o_que_a_empresa_diz`.

## Como uma pessoa faria

- Roda no Chrome de verdade da pessoa, com as contas dela (o Instagram logado mostra o perfil completo), pela
  extensão Agentti. Nada de robô no servidor.
- Ritmo humano e pausas entre as buscas no Google, para respeitar os termos de uso e não ser bloqueado.
- **Chrome do Agentti:** um Chrome separado só para a fila (atalho em Configurações → Extensão Chrome). A janela
  fica atrás das outras, **nunca minimizada**. Minimizada, a página para de desenhar e a fila trava.
- ~15 s por empresa na qualificação (medido em 09/10); ~10 s por lugar na descoberta, mais pausas.
- **Teto diário por pessoa:** 300 buscas no Google e 150 perfis do Instagram (ajustável). No teto, a fila pausa
  até o dia seguinte.

## Limites (diga quando importar)

- Empresa sem site e sem Instagram: o dossiê fica com o Maps e a Receita.
- Rede com muitas unidades: o telefone pode ser de outra loja. Por isso o motor exige o bairro ou o endereço.
- Dossiê é do dia da qualificação (`lido_em`). Para atualizar, qualifique de novo.
- **Qualificação a fundo** (`qualificar` com `profunda: true`): além da home, o Agentti abre até 4 páginas
  internas do site aceito ("Quem somos", "Produtos/Serviços/Cardápio", "Unidades/Lojas", "Trabalhe conosco"),
  clicando nos links da própria página e com tempo de leitura. ~1 min a mais por empresa com site.
  A fundo também lê: os **destaques** do Instagram, a **página do Facebook** aceita (apresentação, categoria,
  recomendação, endereço; precisa do Facebook logado no Chrome do Agentti) e as **notícias** do Google com o nome
  inteiro e a cidade, um sobrenome de sócio ou o site (`o_que_a_empresa_diz.noticias`).
- O Agentti **não envia** mensagens. Campanha automática pelo Instagram e WhatsApp está planejada, não pronta.
