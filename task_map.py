import pandas as pd 
import json 

def coletar_ids(df, coluna):
    ids = []
    for valor in df[coluna].dropna():
        try:
            ids.append(int(valor))
        except ValueError:
            pass
    return ids

def ids_json(chave, ids):
    dados = {chave: ids}
    return json.dumps(dados, indent=4, ensure_ascii=False)

path = r"C:\Users\lucas.martins.6\Documents\monitoramentos EBSERH 2019-2025 SEDE.xlsx"
df = pd.read_excel(path)

listar_ids = coletar_ids(df, "Id da Tarefa")

json_final = ids_json("AUDIN-EBSERH", listar_ids)

if __name__ == "__main__":
    print('JSON gerado com sucesso:')
    print(json_final)
