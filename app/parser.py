import re
def parse_txt_file(filepath):
   with open(filepath, "r", encoding="utf-8") as file:
       lines = file.readlines()[1:]
   columns = [
       "cpf",
       "private",
       "incompleto",
       "data_ultima_compra",
       "ticket_medio",
       "ticket_ultima_compra",
       "loja_mais_frequente",
       "loja_ultima_compra"
   ]
   data = []
   for line in lines:
       parts = re.split(r"\s{2,}", line.strip())
       if len(parts) == len(columns):
           data.append(dict(zip(columns, parts)))
   return data