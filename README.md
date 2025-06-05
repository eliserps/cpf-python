# 🧾 Projeto: Importador de Dados com Validação e Persistência (Python + PostgreSQL)
## 📌 Descrição
Este projeto consiste em um serviço escrito em **Python**, que realiza a leitura, tratamento, validação e persistência de dados a partir de um arquivo `.txt`.
O serviço está completamente containerizado com **Docker e Docker Compose**, utilizando um banco de dados **PostgreSQL** para armazenar os dados processados.
---
## ⚙️ Funcionalidades
- Leitura de arquivo `.txt` com separadores incomuns;
- Parsing de colunas conforme estrutura esperada;
- Validação numérica de **CPF**;
- Higienização de dados (remoção de acentos, espaços extras, etc.);
- Criação automática da tabela no banco;
- Inserção apenas de registros válidos no banco PostgreSQL.
---
## 🧱 Estrutura de Diretórios

CPF-PYTHON/
├── app/
│ ├── db.py # Conexão com o banco, criação de tabela e inserção de dados
│ ├── main.py # Script principal que orquestra o processo
│ ├── parser.py # Lê e faz parsing do arquivo de entrada
│ ├── utils.py # Higienização e normalização de strings
│ ├── validator.py # Validação de CPF usando validate-docbr
│ ├── Dockerfile # Dockerfile da aplicação Python
│ └── docker-compose.yml # Orquestração da aplicação e banco de dados
├── requirements.txt # Dependências do projeto
└── README.md # Este documento
---

## 📥 Entrada
O projeto lê o arquivo `texto.txt`, que deve conter colunas separadas por espaços (com ao menos dois espaços entre os campos).

As colunas esperadas no arquivo são:

- CPF  
- Private  
- Incompleto  
- Data da Última Compra  
- Ticket Médio  
- Ticket da Última Compra  
- Loja Mais Frequente  
- Loja da Última Compra

---

## 🧪 Validação e Higienização
- **Validação de CPF**: é feita utilizando a biblioteca `validate-docbr`, com base apenas na estrutura numérica válida.
- **Higienização dos campos**: remoção de acentos, conversão para minúsculas e remoção de espaços em excesso.

Apenas registros com CPF válido seguem para inserção no banco.
---

## 🧰 Tecnologias Utilizadas
- Python 3.11
- PostgreSQL 15
- Docker
- Docker Compose
- Bibliotecas:
  - `validate-docbr`
  - `psycopg2-binary`

---

## ▶️ Como Executar o Projeto

### 1. Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 2. Passo a passo

Abra o terminal na raiz do projeto e execute:

```bash

# Build dos containers

docker-compose -f app/docker-compose.yml build

# Execução dos containers

docker-compose -f app/docker-compose.yml up
Docker: Accelerated Container Application Development
Docker is a platform designed to help developers build, share, and run container applications. We handle the tedious setup, so you can focus on the code.
 
