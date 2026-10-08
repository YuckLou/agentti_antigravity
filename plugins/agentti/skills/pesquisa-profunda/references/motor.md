# Como o motor do Agentti trabalha

Use para explicar à pessoa de onde vem cada dado, por que algo não foi achado e quanto tempo leva.

## Três camadas

| Camada | O que faz | Custo | Onde roda |
|---|---|---|---|
| **Pré-qualificação** (faixa A/B/C) | Nota do cadastro da Receita: porte, tempo ativa, canal de contato, nome fantasia | grátis | servidor |
| **Qualificação** (`qualificar`) | Acha e prova site, Instagram, WhatsApp, telefone e e-mail; guarda o dossiê | 1 de cota por empresa | Chrome da pessoa |
| **Descoberta** (`descobrir_na_web`) | Acha no Google Maps lugares que a Receita não mostra ou mostra sem contato | 1 de cota por empresa nova | Chrome da pessoa |

## A qualificação, passo a passo

1. **Busca no Google** pelo nome e a cidade. Lê a resposta de IA do Google e os resultados.
2. **Ficha do Google Maps:** telefone e site. Endereço igual ao da Receita = confirmado.
3. **Site:** visita até 2 candidatos. Prova é o CNPJ, o telefone ou o endereço da Receita na página. Site fora
   do ar é descartado.
4. **Instagram:** visita o melhor perfil (e o segundo, se empatar). Prova é o endereço ou o site da empresa no
   perfil. Abre também a página do link da bio (Linktree e parecidas) atrás de WhatsApp.
5. **Bing**, só se o Google e o Maps não trouxerem nem site nem telefone.
6. **Selo:** **confirmado** = a página traz o endereço ou o telefone da Receita; **provável** = indícios fortes
   sem essa prova. O resto fica de fora.
7. **Dossiê:** das páginas aceitas, guarda o que a empresa diz de si (bio, legendas com data, avaliações, texto do
   site). Aparece em `ver_lead` → `o_que_a_empresa_diz`.

## Como uma pessoa faria

- Roda no Chrome de verdade da pessoa, com as contas dela (o Instagram logado mostra o perfil completo), pela
  extensão Agentti. Nada de robô no servidor.
- Ritmo humano e pausas entre as buscas no Google, para respeitar os termos de uso e não ser bloqueado.
- **Chrome do Agentti:** um Chrome separado só para a fila (atalho em Configurações → Extensão Chrome). A janela
  fica atrás das outras, **nunca minimizada**. Minimizada, a página para de desenhar e a fila trava.
- ~30 s por empresa na qualificação; ~10 s por lugar na descoberta, mais pausas.

## Limites (diga quando importar)

- Empresa sem site e sem Instagram: o dossiê fica com o Maps e a Receita.
- Rede com muitas unidades: o telefone pode ser de outra loja. Por isso o motor exige o bairro ou o endereço.
- Dossiê é do dia da qualificação (`lido_em`). Para atualizar, qualifique de novo.
- **Em construção (qualificação profunda):** visitar as páginas internas do site ("Quem somos", "Serviços",
  "Cardápio"), o "Sobre" do Facebook e notícias, até responder as seis perguntas. Hoje o site é lido só na home.
- O Agentti **não envia** mensagens. Campanha automática pelo Instagram e WhatsApp está planejada, não pronta.
