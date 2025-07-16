# 📊 Projeto de Extração e Análise de Dados do YouTube com Python e BigQuery

# 📊 Projeto de Extração e Análise de Dados do YouTube com Python e BigQuery

Este projeto tem como objetivo automatizar a extração de dados de uma playlist do YouTube utilizando a **YouTube Data API v3**, tratar os dados com **Python (pandas)** e enviá-los para uma tabela no **Google BigQuery**, onde será possível realizar análises mais avançadas e visualizações.

---

## 📌 Objetivos

- Extrair dados detalhados de vídeos de uma playlist do YouTube
- Tratar os dados para análise (normalização, limpeza, enriquecimento)
- Persistir os dados no **Google BigQuery** para uso em dashboards e queries SQL
- Automatizar o processo com Python

---

## 🧰 Tecnologias e Bibliotecas Utilizadas

- [Python 3.10+](https://www.python.org/)
- [YouTube Data API v3](https://developers.google.com/youtube/v3)
- [Google Cloud BigQuery](https://cloud.google.com/bigquery)
- [Pandas](https://pandas.pydata.org/)
- [Google Client Library](https://pypi.org/project/google-api-python-client/)
- [google-cloud-bigquery](https://pypi.org/project/google-cloud-bigquery/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## 🔑 Requisitos

- Conta no Google Cloud Platform com projeto e BigQuery habilitado
- Playlist pública no YouTube
- Credenciais de conta de serviço (`.json`)
- Biblioteca `google-api-python-client` configurada com sua chave de API
- Python virtualenv (recomendado)

---

## 📁 Estrutura do Projeto

```bash
📂youtube-playlist-project/
├── BigQuery
├── Dashboard
├── Data
├── Projeto-API
├── .gitgnore
├── requirements.txt
└── README.md

