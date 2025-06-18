import pandas as pd
from sqlalchemy import create_engine, text


class TratarArquivos:
    def __init__(self):
        self.engine = self.postgree()

    def postgree(self):
        host = ""
        port = "5432"
        database = 'curso_ia'
        user = "postgres"
        password = ""
        try:
            db_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
            engine = create_engine(db_url)
            print("Conexão estabelecida com sucesso!")
            return engine
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def tratar_arquivo(self, path, nome_tabela):
        df = pd.read_csv(path, sep=',', encoding='utf-8')

        lista_colunas = []
        for coluna in df.columns:
            coluna = coluna.replace(' ', '_')
            coluna = coluna.replace('-', '_')
            coluna = coluna.replace('/', '_')
            coluna = coluna.replace('(', '_')
            coluna = coluna.replace(')', '_')
            coluna = coluna.replace('"', '')
            coluna = coluna.replace("'", '')
            coluna = coluna.replace(';', '')
            coluna = coluna.replace(':', '')
            coluna = coluna.lower()
            lista_colunas.append(coluna)

        df.columns = lista_colunas
        df.to_sql(nome_tabela, self.engine, schema='stage', if_exists='replace', index=False)


    def inserir_log(self, nivel_log, origem, mensagem, detalhes=None):

        dicionario = {
            'nivel_log': [nivel_log],
            'origem': [origem],
            'mensagem': [mensagem],
            'detalhes': [detalhes]
        }

        df = pd.DataFrame(dicionario)
        df.to_sql('logs', self.engine, schema='stage', if_exists='append', index=False)
