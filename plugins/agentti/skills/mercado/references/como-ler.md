# Como ler `estatisticas_empresas`

## Campos

| Campo | O que é | Como usar |
| :--- | :--- | :--- |
| `total` | estabelecimentos ativos no recorte | o tamanho do mercado visível |
| `empresas_distintas` | raízes de CNPJ distintas (matriz e filiais juntas) | quantas decisões de compra existem |
| `porte` | ME, EPP, DEMAIS, `empresario_individual`, `nao_informado` | `empresario_individual` inclui o MEI: volume de compra pequeno |
| `pre_qualificacao` | faixas A, B e C | A é o quarto de cima do cadastro, C o de baixo |
| `porte_x_faixa` | cruzamento das duas | acha o recorte "grande e bem cadastrado" |
| `pontos_quartis` | quartis dos pontos | mostra se o local é mais forte ou mais fraco que a referência |
| `tempo_ativa` | 10 anos ou mais, 3 a 10, 1 a 3, menos de 1 | empresa nova está escolhendo fornecedor, mas o risco é maior |
| `canal_na_receita` | celular, só fixo, sem telefone | celular costuma ser WhatsApp; a qualificação confirma |
| `com_email_na_receita` | e-mail no cadastro | muitas vezes é do contador, não da empresa |
| `com_nome_fantasia` | tem nome fantasia | sem nome fantasia costuma ser negócio pequeno ou pouco visível |
| `filiais` | estabelecimentos que são filial | alto = presença de redes |
| `capital_social` | p25, mediana, p75, p90 | declarado na abertura; compara empresas, não é faturamento |
| `ramos` | contagem por CNAE | mostra qual ramo pesa mais no total |
| `bairros`, `municipios` | onde estão | concentração; bom para rota de visita |
| `distancia` | só com raio: até 1 km, 1 a 2, 2 a 3, 3 a 5, 5 a 10, acima | quanto do mercado está perto |
| `area_km2`, `densidade_por_km2` | só com raio | compara locais de tamanhos diferentes |

## A faixa (pré-qualificação)

Pontos só do cadastro da Receita: porte até 25, tempo ativa até 30, celular 25 ou fixo 15, nome fantasia 12,
e-mail 8. A ≥ 78, B ≥ 60, C abaixo. Os cortes vieram dos quartis de um mercado de referência (confeitarias num
raio de 3 km numa capital), então em outro ramo a distribuição pode ser bem diferente. Isso é informação: um
local com 40% em A tem cadastro mais forte que a referência.

## Limitações que sempre valem a pena dizer

- A base mostra quem existe e está ativo, não quem compra.
- MEI e empresário individual aparecem como `empresario_individual`; o volume de compra costuma ser pequeno.
- Capital social é declarado na abertura e raramente atualizado.
- E-mail da Receita costuma ser do escritório de contabilidade.
- Endereço é o do cadastro; comércio que mudou e não atualizou aparece no lugar antigo.

## Recortes que costumam funcionar

| Objetivo | Recorte |
| :--- | :--- |
| Poucos e bons, para visita | EPP e Demais, faixa A, raio curto |
| Volume para WhatsApp | faixa A e B, com celular |
| Redes | somente matriz, e depois olhar `filiais` |

Tempo ativa não é filtro das ferramentas: aparece na estatística e nos motivos da faixa de cada empresa.
