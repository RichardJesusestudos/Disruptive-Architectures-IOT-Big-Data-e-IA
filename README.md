# Pipeline de IoT e Big Data - Análise de Sensores Térmicos

Projeto desenvolvido para a disciplina de **Disruptive Architectures: IoT, Big Data e IA**.

## Sobre o Projeto
Este projeto consiste num pipeline de ETL (*Extract, Transform, Load*) criado para processar um conjunto de dados de sensores IoT (`IOT-temp.csv`, com cerca de 97 mil registos). O sistema extrai os dados, faz o tratamento e limpeza com Python, armazena as informações num banco de dados relacional via Docker (PostgreSQL) e disponibiliza um painel interativo em Streamlit para visualização.

## Tecnologias Utilizadas
- **Python 3.12** (Pandas, SQLAlchemy, Psycopg2)
- **Docker** (PostgreSQL)
- **Streamlit & Plotly** (Dashboard e visualização de dados)

## Estrutura do Repositório
```text
projeto-iot-pipeline/
├── data/
│   └── IOT-temp.csv
├── src/
│   ├── pipeline.py
│   └── app.py
└── README.md
```

## Como Executar o Projeto

Certifique-se de que tem o **Docker Desktop** em execução e o **Python 3.12** instalado no seu ambiente.

### 1. Iniciar o Banco de Dados (Docker)
Execute o comando abaixo no terminal para subir o contentor do PostgreSQL com a base de dados:
```bash
docker run --name postgres-iot -e POSTGRES_PASSWORD=IoTSecure_9#vX$2026!kL -p 5432:5432 -d postgres
```

### 2. Executar o Pipeline ETL
Rode o script em Python para ler o ficheiro CSV e carregar os dados para a tabela do PostgreSQL:
```bash
py -3.12 src/pipeline.py
```

### 3. Iniciar o Painel Streamlit
Inicie a aplicação web para visualizar os dados e gráficos interativos:
```bash
py -3.12 -m streamlit run src/app.py
```
O painel abrirá automaticamente no navegador em `http://localhost:8501`.