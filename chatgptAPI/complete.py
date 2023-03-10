import os
import openai

openai.api_key_path= "chatgpt/.localfolderenv"
openai.api_key= os.getenv("OPENAI_API_KEY")

question = "make questions about Brazilian Empire"
response = openai.Completion.create(
  model="text-davinci-003",
  prompt= question,
  temperature=0.6,
  max_tokens=150,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)

print( str(response['choices'][0]['text']))


response = openai.Completion.create(
  model="text-davinci-003",
  prompt="\nO ministro da Fazenda, Fernando Haddad, anunciou nesta sexta-feira (10) um acordo com os governadores dos estados para compensar as perdas com a redução da alíquota do ICMS, tributo estadual, sobre combustíveis no valor de R$ 26,9 bilhões. Até a semana passada, esse valor ainda não tinha sido fechado. Os valores serão abatidos da dívida com a União dos estados. Aqueles que não têm dívidas, receberão aportes de recursos. Inicialmente, segundo o presidente do Comitê Nacional de Secretários de Fazenda dos Estados e do DF, Carlos Eduardo Xavier, os estados haviam pedido R$ 45 bilhões, valor que caiu, posteriormente, para R$ 37 bilhões. Os estados chegaram a informar que a limitação da alíquota em 18% gerou perdas de R$ 45 bilhões nos últimos seis meses de 2022, mas o acordo foi fechado no valor da última proposta feita pelo Ministério da Fazenda, em R$ 26,9 bilhões. \"Chegamos a um número que, em um acordo... Quando é um acordo, nunca é satisfatório para ninguém. Conta que foi feita com base em parâmetros técnicos. Tecnicamente, o trabalho foi intenso\", disse o ministro Haddad a jornalistas. Segundo o governador do Piauí, Rafael Fonteles, os estados não poderiam discutir a reforma tributária, negociada no Congresso Nacional, sem resolver as pendências de combustíveis de 2022. \"Os estados são interessados nessa questão [reforma tributária], Brasil tá atrasado na questão tributária, essa reforma a gente acredita muito que tem condição de ser votada e aprovada esse ano\", afirmou.",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(str(response))