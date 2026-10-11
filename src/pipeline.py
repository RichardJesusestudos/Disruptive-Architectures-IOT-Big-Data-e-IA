import os
import pandas as pd
from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASS = "IoTSecure_9#vX!kL"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def run_pipeline():
    print("[INFO] A iniciar o pipeline ETL de IoT...")
    data_dir = "data"
    if not os.path.exists(data_dir):
        print(f"[ERRO] A pasta '{data_dir}' não foi encontrada.")
        return

    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    if not csv_files:
        print(f"[ERRO] Nenhum ficheiro CSV encontrado na pasta '{data_dir}'.")
        return

    csv_path = os.path.join(data_dir, csv_files[0])
    print(f"[INFO] A ler o ficheiro: {csv_path}")

    df = pd.read_csv(csv_path)
    print(f"[INFO] Dados extraídos com sucesso. Total de linhas: {len(df)}")

    df.columns = [c.strip().lower().replace(' ', '_').replace('-', '_') for c in df.columns]

    print("[INFO] A estabelecer ligação ao PostgreSQL e a carregar os dados...")
    engine = create_engine(DATABASE_URL)
    table_name = "iot_temperature_readings"
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"[SUCESSO] Dados processados e inseridos com sucesso na tabela '{table_name}' do PostgreSQL!")

if __name__ == "__main__":
    run_pipeline()
