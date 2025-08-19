import requests
import pandas as pd 
import os
from dotenv import load_dotenv
from datetime import date 
from itertools import chain 


load_dotenv(dotenv_path='.env')

class Requests:
    def __init__(self):
        self.chave_api = os.getenv('chave_api')
        if not self.chave_api:
            raise ValueError("API key not found. Please set 'chave_api' in your .env.development file.")

        self.base_url = 'https://eaud.cgu.gov.br/api/auth/monitoramento?apenasAbertas=false&exibirColunaPendencias=false&apenasModificadasNosUltimos30Dias=false&colunaOrdenacao=id&direcaoOrdenacao=DESC&tamanhoPagina=15&offset=0&unidadesAuditadas=30481%2C30480%2C30488&periodoInicialDataInicio=2025-01-01&incluirUnidadesAuditadasInferiores=true&contarRegistros=true&colunasSelecionadas=id%2Csituacao%2Cestado%2Ctitulo%2CdtRealizadaInicio%2CorigemRecomendacao%2CdtLimite%2CsiglaUnidadeAuditada%2CunidadesDeAuditoria%2Cdetalhes%2Cprovidencia%2CtextoUltimaManifestacao%2CtextoUltimoPosicionamento%2CdtLimiteInicial&mostrarTarefaBloqueadaPgd=true#lista'
        self.headers = {'chave-api':self.chave_api,'Accept-Enconding':'gzip,deflate'}
        self.df = None


    def get_data(self):
   
        print('Iniciando a coleta de dados da API...')
       
        response = requests.get(self.base_url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            tarefas = data.get("data",[])
        else:
            print(f"Erro ao obter dados da tarefa {id}: {response.status_code}")
            self.df = pd.DataFrame()
            return self.df 
    
        self.df = pd.json_normalize(tarefas)
        return self.df 
    
    def save_csv(self, nome_arquivo='monitoramento_api.xlsx'):
        if self.df is not None:
            self.df.to_excel(nome_arquivo, index=False)
            print(f"Dados salvos em {nome_arquivo}")
        else:
            print("Nenhum dado para salvar. Execute get_data() primeiro.")

if __name__ == "__main__":
    req = Requests()
    df = req.get_data()
    if df is not None:
        print(df.head())  
        req.save_csv()  