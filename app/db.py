import psycopg2
import os
def connect():
   return psycopg2.connect(
       dbname=os.getenv("POSTGRES_DB", "clientes"),
       user=os.getenv("POSTGRES_USER", "user"),
       password=os.getenv("POSTGRES_PASSWORD", "senha"),
       host="db"
   )
def create_table():
   conn = connect()
   cur = conn.cursor()
   cur.execute("""
       CREATE TABLE IF NOT EXISTS clientes (
           cpf VARCHAR(11) PRIMARY KEY,
           private BOOLEAN,
           incompleto BOOLEAN,
           data_ultima_compra TEXT,
           ticket_medio TEXT,
           ticket_ultima_compra TEXT,
           loja_mais_frequente TEXT,
           loja_ultima_compra TEXT
       );
   """)
   conn.commit()
   conn.close()
def insert_data(data):
   conn = connect()
   cur = conn.cursor()
   for row in data:
       cur.execute("""
           INSERT INTO clientes (cpf, private, incompleto, data_ultima_compra,
               ticket_medio, ticket_ultima_compra, loja_mais_frequente, loja_ultima_compra)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
           ON CONFLICT (cpf) DO NOTHING;
       """, (
           row["cpf"],
           row["private"] == "1",
           row["incompleto"] == "1",
           row["data_ultima_compra"],
           row["ticket_medio"],
           row["ticket_ultima_compra"],
           row["loja_mais_frequente"],
           row["loja_ultima_compra"],
       ))
   conn.commit()
   conn.close()