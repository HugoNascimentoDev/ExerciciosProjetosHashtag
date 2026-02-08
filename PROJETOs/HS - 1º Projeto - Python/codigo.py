# Passo a passo do projeto





# Passo 1 - Pegar cada base de dados

import pandas as pd # importando a biblioteca pandas e nomeando como pd
import os

lista_arquivos_diretorio = os.listdir() # Verificando todas as bases de dados armanezadas no diretório

lista_lojas = [] # criando a lista de lojas

for arquivo in lista_arquivos_diretorio: # percorrendo a lista de arquivos no diretório e separando apenas as bases de dados das lojas
    if "xlsx" in arquivo:
        cidade = arquivo.replace('Loja ', '').replace('.xlsx', '') # tratando o nome do arquivo antes de adicionar o nome na lista de lojas
        lista_lojas.append(cidade) # adicionando apenas o nome das cidades na lista de lojas

# Passo 2 - Para cada base de dados
# Calcular o faturamento total (somar todos os valores da coluna de vendas)

total_faturamentos = {} #criando um dicionário para armazenar o total de faturamentos

for loja in lista_lojas: # acessando cada base de dados das lojas
    vendas_loja_df = pd.read_excel(f"Loja {loja}.xlsx") # df = dataframe (tabelas do pandas) - acessando e lendo cada base de dados
    faturamento_total_cidade = sum(vendas_loja_df["Vendas"]) # criando uma váriavel para armazenar o total da coluna "vendas" de cada base de dados
    total_faturamentos[loja.upper()] = faturamento_total_cidade # adicionando o valor total de faturamentos dentro de cada loja no dicionacio total_faturamentos
   
# Passo 3 - Criar um ranking com o faturamento total de todas as lojas

#criando um dataframe através do dicionário total_faturamentos e criando uma tabela com as informações
ranking_df = pd.DataFrame.from_dict(total_faturamentos, orient= "index", columns= ["Total Faturamento"])
#Colocando a tabela em ordem descrente através da coluna Total Faturamento
ranking_df = ranking_df.sort_values(by= "Total Faturamento", ascending= False)

#formatando o texto
ranking_df = ranking_df.map("R$ {:,.2f}".format)

# Passo 4 - Enviar por email esse ranking para a diretoria

#criando a mensagem
mensagem = f"""
Prezados,

Segue em anexo o ranking de faturamento das nossas Lojas.

Ranking: 

{ranking_df.to_string().replace(" ", "-").replace(',','.')} 

Qualquer dúvida, estou à disposição.

Att.,
Hugo Dev
"""

# to_string ele formata a tabela em texto


# como enviar por email
# 4 grandes formas

# yagmail. - a mais direta e simples - utilizado quando queremos utilizar uma mensagem simples
# smtplib - não é tão direto, mas é bem personalizado, ele consegue anexar, editar e vários ajustes
# pyautogui - automação por RPA - só usamos em automaçõ~es que já são para RPA, não pode utilizar o computador em quanto estamos fazendo executando o código
# outlook - quando a empresa utiliza o outlook como ferramenta padrão

import yagmail
from chave import senha #acessa o arquivo "chave" e para trazer a váriavel senha para não ficar diretamente no arquivo

#acessando um email, através do usuário e da funcionalidade senha do app ( a senha foi armazenada no arquivo chave)
usuario = yagmail.SMTP("hugopythondev@gmail.com", senha)
#enviando o email
usuario.send(
    to= "hugopythondev+diretoria@gmail.com", # para quem é o email
    subject= "Ranking de Vendas por Loja", # assunto do email
    contents=  mensagem #conteúdo do email
)

#como rodar código python semanalmente

