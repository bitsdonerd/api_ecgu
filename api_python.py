import requests
import pandas as pd 
import os
from dotenv import load_dotenv
from datetime import date 
from itertools import chain 


load_dotenv(dotenv_path='.env.development')

# Teste de request 
json_final = {
    "Auditoria Interna": [
        1318042,
        1318072,
        1318096
    ],
    "Auditoria Externa": [
        1447960,
        1447963
    ],
    "TCU": [
        1485049,
        1546558
    ]
}

class Requests:
    def __init__(self):
        self.chave_api = os.getenv('chave_api')
        if not self.chave_api:
            raise ValueError("API key not found. Please set 'chave_api' in your .env.development file.")

        self.base_url = 'https://eaud.cgu.gov.br/api/auth/tarefa/'
         #https://eaud.cgu.gov.br/api/auth/tarefa/tarefasAssociadas?colunaOrdenacao=id&direcaoOrdenacao=ASC&tamanhoPagina=15&offset=0&idTarefaAssociada={}&exibirColunaPendencias=true&colunasSelecionadas=id%2Cassunto%2Cestado%2Catividade%2Ctitulo&apenasAbertas=false&_=1727449385295
        self.headers = {'chave-api':self.chave_api,'Accept-Enconding':'gzip,deflate'}
        self.task = json_final
        self.df = None
        self.id = None

    def get_data(self):
        tabela = []
        print('Iniciando a coleta de dados da API...')
       
        self.id = list(chain.from_iterable(self.task.values())) 
    
        for id in self.id:
            url = self.base_url.format(id=id)
            response = requests.get(url, headers=self.headers)
    
            if response.status_code == 200:
                data = response.json()
                tabela.append(data)
            else:
                print(f"Erro ao obter dados da tarefa {id}: {response.status_code}")
    
        self.df = pd.DataFrame(tabela)
        return self.df 
    
    def save_csv(self, nome_arquivo='monitoramento_api.csv'):
        if self.df is not None:
            self.df.to_excel(nome_arquivo, index=False)
            print(f"Dados salvos em {nome_arquivo}")
        else:
            print("Nenhum dado para salvar. Execute get_data() primeiro.")

if __name__ == "__main__":
    req = Requests()
    df = req.get_data()
    print(df.head())  
    req.save_csv()  