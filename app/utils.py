import unicodedata
def normalize_string(s: str) -> str:
   if s == "NULL":
       return None
   return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("utf-8").strip()