import unittest

from bank import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """
        Sets up a bank account for a single person.
        """
        self.name = "John Doe"
        self.account = BankAccount(self.name)

    def test_create_account(self):
        """
        Checking that the created account has the correct information.
        """
        # Checks that the account created is a BankAccount type
        self.assertIsInstance(self.account, BankAccount, "The created bank account is not an instance of BankAccount")

        # Checks that the name was processed correctly
        self.assertEqual(self.name, self.account.account_holder,
                         "The name of the account holder does not match the given name when creating BankAccount")

        # Check that the balance is set to 0 by default
        self.assertEqual(0, self.account.balance, "Balance should be set to 0 when BankAccount is initialised.")

    def test_account_info(self):
        """
        Checks that getting the account information is correctly given.
        Focuses on testing the ``account_info()`` method in BankAccount.
        """
        account_info = self.account.account_info()

        # Checks that the information given is correct/as expected
        self.assertEqual(self.name, account_info.name, "Names from account_info() do not match the given name.")
        self.assertEqual(0, account_info.balance, "Initialised BankAccount balance should be 0.")

        # Checks that the information can be used for comparisons
        new_account = BankAccount(self.name)
        self.assertEqual(account_info, new_account.account_info(),
                         "account_info() should be the same on both bank accounts.")

        other_account = BankAccount("Jane Doe")
        self.assertNotEqual(account_info, other_account.account_info(),
                            "account_info() should be different for two different people.")

    def test_deposit(self):
        """
        Testing the ``deposit()`` method in BankAccount
        """
        # Checks that you cannot deposit a negative value
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

        # Checks that you cannot deposit nothing
        with self.assertRaises(ValueError):
            self.account.deposit(0)

        # Checks that you can deposit money
        deposited = 100
        self.account.deposit(deposited)

        self.assertEqual(deposited, self.account.balance, "Balance does not match what has been deposited.")

        deposit = 50
        self.account.deposit(deposit)
        deposited += deposit

        self.assertEqual(deposited, self.account.balance, "Balance does not match after depositing twice.")

    def test_withdraw(self):
        """
        Testing the ``withdraw()`` method in BankAccount
        """
        # Checks that a negative amount of money cannot be withdrawn
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

        # Checks that you cannot withdraw nothing
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

        # Adds a balance to the account beforehand
        initial_balance = 1000000
        self.account.deposit(initial_balance)

        # Withdraw a set amount
        requested_amount = 100
        withdrawn = self.account.withdraw(requested_amount)
        self.assertEqual(requested_amount, withdrawn, "Requested amount of money was not given when withdrawn.")
        self.assertEqual(initial_balance - requested_amount, self.account.account_info().balance,
                         "Balance after withdrawing is not as expected.")
        total_withdrawn = withdrawn

        # Checks withdrawing a second time works as expected
        requested_amount = 50
        withdrawn = self.account.withdraw(requested_amount)
        self.assertEqual(requested_amount, withdrawn, "Requested amount of money was not given when withdrawn.")
        total_withdrawn += withdrawn
        self.assertEqual(initial_balance - total_withdrawn, self.account.account_info().balance,
                         "Balance after withdrawing is not as expected.")

        # Check that the account cannot be overdrawn
        with self.assertRaises(ValueError):
            self.account.withdraw(initial_balance)

    def test_create_two_accounts(self):
        name = "Jane Doe"
        account = BankAccount(name)

        # Checks that the two accounts are not considered the same
        self.assertNotEqual(self.account, account, "A new object should not be the same.")

        # Checks that the names are both different
        self.assertNotEqual(self.account.account_info(), account.account_info(),
                            "Account information should be different.")


if __name__ == '__main__':
    unittest.main()
