import pandas as pd
import json

def coletar_ids_por_setor(df, coluna_setor, coluna_id):
    ids_por_setor = {}

    for _, row in df.iterrows():
        setor = row[coluna_setor]
        tarefa_id = row[coluna_id]

        # Ignorar valores nulos
        if pd.isna(setor) or pd.isna(tarefa_id):
            continue

        try:
            tarefa_id = int(tarefa_id)  # garantir número
        except ValueError:
            continue

        if setor not in ids_por_setor:
            ids_por_setor[setor] = []

        ids_por_setor[setor].append(tarefa_id)

    return ids_por_setor


def ids_json(dados):
    return json.dumps(dados, indent=4, ensure_ascii=False)


path = r"C:\Users\lucas.martins.6\Documents\monitoramentos EBSERH 2019-2025 SEDE.xlsx"
df = pd.read_excel(path)

# Criar dicionário setor -> lista de IDs
dados_por_setor = coletar_ids_por_setor(df, "Origem da Recomendação", "Id da Tarefa")

# Transformar em JSON
json_final = ids_json(dados_por_setor)

if __name__ == "__main__":
    print('JSON gerado com sucesso:')
    print(json_final)

