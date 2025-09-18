from unittest import TestCase

from bank import CheckingAccount


class TestCheckingAccount(TestCase):
    def setUp(self):
        self.name = "John Doe"
        self.transaction_fee = 12
        self.account = CheckingAccount(self.name, self.transaction_fee)
        self.balance = 100000
        self.account.deposit(self.balance)

    def test_withdraw(self):
        withdraw = 100
        expected_balance = self.balance - self.transaction_fee - withdraw

        # Withdraw money from the account
        amount_given = self.account.withdraw(withdraw)

        # Get the balance after withdrawing from the account
        actual_balance = self.account.account_info().balance

        # Checks that the accountholder got the amount they wanted to withdraw (does not include transaction fees)
        self.assertEqual(withdraw, amount_given, "Amount withdrawn is not the same as requested.")
        # Checks that the balance reflects the amount withdrawn alongside transaction fees
        self.assertEqual(expected_balance, actual_balance, "Expected balance is not the same what is on the account.")

        # Try to withdraw from the entire account
        withdraw = actual_balance

        with self.assertRaises(ValueError):
            self.account.withdraw(withdraw)


        # Remove the transaction fee from the amount wanted to withdraw
        withdraw -= self.transaction_fee

        amount_given = self.account.withdraw(withdraw)
        actual_balance = self.account.account_info().balance

        # Checks that the accountholder got the amount they requested
        self.assertEqual(withdraw, amount_given, "Amount withdrawn is not the same as requested.")
        # Checks the account is empty after withdrawing everything whilst not including the fees.
        self.assertEqual(0, actual_balance, "Account is not empty after withdrawing everything.")

    def test_invalid_transaction_fee(self):
        # Checks that the transaction fee cannot be negative when creating the account
        with self.assertRaises(ValueError):
            CheckingAccount(self.name, -self.transaction_fee)

