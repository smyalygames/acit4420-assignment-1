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
        expected_interest = expected_balance - self.balance

        # Apply interest to the account
        interest_gained = self.account.apply_interest()

        # Gets the balance in the account after applying the interest
        actual_balance = self.account.account_info().balance

        # Checks the amount of interest gained
        self.assertEqual(expected_interest, interest_gained, "Interest gained is not as expected.")

        # Checks the balance of the account is correct
        self.assertEqual(expected_balance, actual_balance,
                         "Balance in the account is not the same as the expected balance.")

    def test_invalid_interest(self):
        # Can't have a negative interest rate
        with self.assertRaises(ValueError):
            SavingsAccount(self.name, interest_rate=-0.55)

        # Cannot have zero interest rate
        with self.assertRaises(ValueError):
            SavingsAccount(self.name, interest_rate=0.0)
