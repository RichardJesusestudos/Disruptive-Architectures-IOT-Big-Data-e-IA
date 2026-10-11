import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.set_page_config(page_title="IoT Big Data Dashboard", layout="wide")

DATABASE_URL = "postgresql+psycopg2://postgres:IoTSecure_9#vX!kL@localhost:5432/postgres"

@st.cache_data
def load_data_from_view(view_name):
    engine = create_engine(DATABASE_URL)
    query = f"SELECT * FROM {view_name}"
    return pd.read_sql(query, engine)

st.title("Dashboard de Temperaturas IoT e Big Data")
st.markdown("Visualizacao analitica baseada em Views SQL geradas automaticamente pelo pipeline.")

st.header("Media de Temperatura por Dispositivo")
df_avg_temp = load_data_from_view('avg_temp_por_dispositivo')
if not df_avg_temp.empty:
    fig1 = px.bar(df_avg_temp, x='device_id', y='avg_temp', labels={'device_id': 'Dispositivo / Sala', 'avg_temp': 'Temp Media (C)'})
    fig1.update_traces(width=0.3)
    st.plotly_chart(fig1, width='stretch')
else:
    st.warning("Sem dados disponiveis na view.")

st.divider()

st.header("Leituras por Hora do Dia")
df_leituras_hora = load_data_from_view('leituras_por_hora')
if not df_leituras_hora.empty:
    fig2 = px.line(df_leituras_hora, x='hora', y='contagem', labels={'hora': 'Hora do Dia', 'contagem': 'N. de Leituras'}, markers=True)
    st.plotly_chart(fig2, width='stretch')
else:
    st.warning("Sem dados disponiveis na view.")

st.divider()

st.header("Temperaturas Maximas e Minimas por Dia")
df_temp_max_min = load_data_from_view('temp_max_min_por_dia')
if not df_temp_max_min.empty:
    fig3 = px.line(df_temp_max_min, x='data', y=['temp_max', 'temp_min'], labels={'data': 'Data', 'value': 'Temperatura (C)', 'variable': 'Metrica'})
    st.plotly_chart(fig3, width='stretch')
else:
    st.warning("Sem dados disponiveis na view.")
