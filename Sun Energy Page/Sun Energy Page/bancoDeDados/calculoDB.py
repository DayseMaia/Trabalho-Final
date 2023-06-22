# Utlizar só para transformar os dados do arquivo excel em banco de dados
import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="host",
    database="databasename",    # database="dados_calculo", mudei para sun
    user="username",
    password="password"
)

tabelaSql = f''' CREATE TABLE dados_calc (
	id INT,
	longitude NUMERIC,
	latitude NUMERIC,
	cidade VARCHAR(50),
	estado VARCHAR(50),
	media_anual INT,
	media_jan INT,
	media_fev INT,
	media_mar INT,
	media_abr INT,
	media_mai INT,
	media_jun INT,
	media_jul INT,
	media_ago INT,
	media_set INT,
	media_out INT,
	media_nov INT,
	media_dez INT
)

'''
def criarTabelaCalculos():
    cursor = conn.cursor()
    cursor.execute(tabelaSql)
    conn.commit()
    conn.close()

#criarTabelaCalculos()

df = pd.read_excel("static/dados_calculo.xlsx")

data = [tuple(x) for x in df.to_numpy()]

cur = conn.cursor()

insert_query = "INSERT INTO dados_calc (id, longitude, latitude, cidade, estado, media_anual, media_jan, media_fev, media_mar, media_abr, media_mai, media_jun, media_jul, media_ago, media_set, media_out, media_nov, media_dez) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
cur.executemany(insert_query, data)

conn.commit()
conn.close()
