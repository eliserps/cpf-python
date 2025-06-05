from app.parser import parse_txt_file
def test_parse_txt_file(tmp_path):
   test_file = tmp_path / "dummy.txt"
   test_file.write_text("CPF  PRIVATE  INCOMPLETO\n123.456.789-00  0  1\n")
   result = parse_txt_file(str(test_file))
   assert len(result) == 1
   assert result[0]["cpf"] == "123.456.789-00"
   assert result[0]["private"] == "0"
   assert result[0]["incompleto"] == "1"