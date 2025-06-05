#!/bin/sh
echo "Aguardando o banco de dados iniciar..."
# tenta conectar no PostgreSQL até conseguir
while ! nc -z db 5432; do
 sleep 1
done
echo "Banco de dados disponível, iniciando aplicação..."
python app/main.py
