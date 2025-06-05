from parser import parse_txt_file
from validator import is_valid_cpf
from db import insert_data, create_table
from utils import normalize_string
def main():
   print("Lendo dados...")
   data = parse_txt_file("texto.txt")
   print("Validando e higienizando...")
   valid_data = []
   for row in data:
       cpf = row["cpf"]
       if is_valid_cpf(cpf):
           row["cpf"] = cpf.replace(".", "").replace("-", "")
           for k, v in row.items():
               row[k] = normalize_string(v)
           valid_data.append(row)
   print(f"Inserindo {len(valid_data)} registros no banco...")
   create_table()
   insert_data(valid_data)
   print("Pronto!")
if __name__ == "__main__":
   main()