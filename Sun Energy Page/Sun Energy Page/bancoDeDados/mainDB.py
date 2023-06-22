###############################################################################
############# pré-requisitos para rodar o arquivo mainDB.py  ##################
###############################################################################
# instale as seguintes bibliotecas no padrão python:
# psycopg2

from bancoDeDados.classConexao import *
from bancoDeDados.sqlScript import sqltabelas
from bancoDeDados.env import * 

# criada conexão com o banco de dados:
conexao = Conexao(envdbname, envdbhost, envdbport, envdbuser, envdbpassword)

def criarTabelas():
    resultado = conexao.manipularBanco(sqltabelas)
    if resultado:
        print("tabelas criadas com sucesso")
    else:
        print("ocorreu um erro na criação de tabelas")

#////////////// inicio /////////////////

criarTabelas()
