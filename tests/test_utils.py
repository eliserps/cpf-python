from app.utils import normalize_string
def test_normalize_string():
   assert normalize_string(" João ") == "joao"
   assert normalize_string("CAFÉ") == "cafe"