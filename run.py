import pandas as pd
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://postgres:IoTSecure_9#vX!kL@localhost:5432/postgres"

def execute():
    engine = create_engine(DATABASE_URL)
    
    with engine.begin() as conn:
        conn.execute(text("DROP VIEW IF EXISTS avg_temp_por_dispositivo CASCADE;"))
        conn.execute(text("DROP VIEW IF EXISTS leituras_por_hora CASCADE;"))
        conn.execute(text("DROP VIEW IF EXISTS temp_max_min_por_dia CASCADE;"))
        
    df = pd.read_csv("data/IOT-temp.csv")
    df.columns = [col.strip().lower() for col in df.columns]
    df.to_sql("iot_temperature_readings", engine, if_exists="replace", index=False)
    
    with engine.begin() as conn:
        conn.execute(text("CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS SELECT \"room_id/id\" AS device_id, ROUND(CAST(AVG(temp) AS NUMERIC), 2) AS avg_temp FROM iot_temperature_readings GROUP BY \"room_id/id\";"))
        conn.execute(text("CREATE OR REPLACE VIEW leituras_por_hora AS SELECT EXTRACT(HOUR FROM TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS hora, COUNT(*) AS contagem FROM iot_temperature_readings GROUP BY hora ORDER BY hora;"))
        conn.execute(text("CREATE OR REPLACE VIEW temp_max_min_por_dia AS SELECT CAST(TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI') AS DATE) AS data, MAX(temp) AS temp_max, MIN(temp) AS temp_min FROM iot_temperature_readings GROUP BY data ORDER BY data;"))
        
    print("Pipeline executado e views criadas com sucesso.")

if __name__ == "__main__":
    execute()
