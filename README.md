# Pipeline de IoT e Big Data - Análise de Sensores Térmicos

Projeto desenvolvido para a disciplina de **Disruptive Architectures: IoT, Big Data e IA**.

---

## 🎬 Vídeo de Apresentação (Pitch)

O vídeo de demonstração do projeto, com a explicação da arquitetura, do pipeline e do dashboard interativo, está disponível no YouTube:

▶️ **[Assistir ao Vídeo do Projeto no YouTube](https://youtu.be/heWTm9ut4JU)**

---

## 📦 Repositório do GitHub

O código-fonte completo, documentação e scripts encontram-se disponíveis no repositório oficial:
🔗 **[Repositório no GitHub](https://github.com/RichardJesusestudos/Disruptive-Architectures-IOT-Big-Data-e-IA)**

---

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
├── docs/
│   └── relatorio_teorico.pdf
├── sql/
│   └── .gitkeep
├── src/
│   ├── pipeline.py
│   └── app.py
├── README.md
└── run.py