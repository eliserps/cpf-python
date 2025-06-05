import unittest
from validator import is_valid_cpf
class TestCPFValidation(unittest.TestCase):
   def test_valid_cpf(self):
       self.assertTrue(is_valid_cpf("041.091.641-25"))
   def test_invalid_cpf(self):
       self.assertFalse(is_valid_cpf("123.456.789-00"))
if __name__ == "__main__":
   unittest.main()