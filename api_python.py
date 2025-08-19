import requests
import pandas as pd 
from datetime import date 
from itertools import chain 
from task_map import json_final

class Requests:
    def __init__(self):
        self.chave_api = '529f6149ed146ecde0ed5592e1eea2e3'
        self.base_url = 'https://eaud.cgu.gov.br/api/auth/tarefa/gantt/{id}/dto/json'
        self.headers = {'chave-api': self.chave_api, 'Accept-Encoding': 'gzip,deflate'}
        self.df = None

        
        self.task_id = json_final

    def create_df(self):
        tabela = []
        all_ids = list(chain.from_iterable(self.task_id.values())) 

        for task_id in all_ids:
            url = self.base_url.format(id=task_id)
            response = requests.get(url, headers=self.headers)

            if response.status_code == 200:
                data = response.json()
                tabela.append(data)
            else:
                print(f"Erro ao obter dados da tarefa {task_id}: {response.status_code}")

        self.df = pd.DataFrame(tabela)
        return self.df

    def salvar_csv(self, nome_arquivo="tarefas_filtradas.csv"):
        if self.df is not None:
            self.df.to_csv(nome_arquivo, index=False, encoding="utf-8-sig")
            print(f"Arquivo {nome_arquivo} salvo com sucesso!")
        else:
            print("Nenhum DataFrame disponível para salvar.")

    