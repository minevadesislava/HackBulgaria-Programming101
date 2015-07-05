import unittest
from bank_account import BankAccount

class BankAccountTest(unittest.TestCase):

    def test_create_new_account(self):
        account = BankAccount("Rado", 0, "$")
        self.assertTrue(isinstance(account, BankAccount))

    def test_account_name_is_string(self):
    	pass

    def test_create_int_value_from_bill(self):
        account = BankAccount("Rado", 0, "$")
        self.assertEqual(int(account.balance), 0)

    def test_value_error_from_negative_account(self):
    	with self.assertRaises(ValueError)
    	account = BankAccount("Rado", 0, "$")

    def test_initial







if __name__ == '__main__':
	unittest.main()

