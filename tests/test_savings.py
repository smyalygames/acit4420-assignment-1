from unittest import TestCase

from bank import SavingsAccount


class TestSavingsAccount(TestCase):
    def setUp(self):
        self.name = "John Doe"
        self.interest = 0.05
        self.account = SavingsAccount(self.name, self.interest)
        self.balance = 100000
        self.account.deposit(self.balance)

    def test_apply_interest(self):
        expected_balance = self.balance * (1 + self.interest)
        self.account.apply_interest()

        self.assertEqual(expected_balance, self.account.account_info().balance, "The expected balance is not the same what is on the account.")
