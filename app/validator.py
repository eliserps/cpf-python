from validate_docbr import CPF
def is_valid_cpf(cpf: str) -> bool:
   cpf_clean = cpf.replace(".", "").replace("-", "")
   return CPF().validate(cpf_clean)