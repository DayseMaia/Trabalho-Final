# Criando conexão com o banco de dados
import psycopg2

class Conexao:
    def __init__(self, dbname, host, port, user, password):
        
        self._dbname = dbname
        self._host = host
        self._port = port
        self._user = user
        self._password = password

    def consultarBanco(self,sql):
        
        try:
            conn = psycopg2.connect(dbname = self._dbname, host = self._host,port = self._port, user = self._user, password = self._password)
            cursor = conn.cursor()

            cursor.execute(sql)

            resultado = cursor.fetchall()
            
            cursor.close()
            conn.close()

            return resultado
        
        except(psycopg2.Error) as error:
            print("Ocorreu um erro ao tentar a conexão", error)

            return False

    def manipularBanco(self,sql):
        try:
            conn = psycopg2.connect(dbname = self._dbname, host = self._host,port = self._port, user = self._user, password = self._password)
            cursor = conn.cursor()

            cursor.execute(sql)

            conn.commit()

            cursor.close()
            conn.close()

            return True

        except(psycopg2.Error) as error:
            print("Ocorreu um erro ao tentar a conexão", error)
        
            return False
            