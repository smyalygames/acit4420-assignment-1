from dataclasses import dataclass


@dataclass
class AccountInformation:
    name: str
    balance: int


class BankAccount:

    def __init__(self, name: str):
        """
        A normal bank account for a person.
        :param name: The name of the person
        """
        self.account_holder = name
        self.balance = 0  # FIXME handle 2dp, and make sure not to have floating point errors

    def account_info(self) -> AccountInformation:
        """
        Gets the name and balance of the account holder.
        :return:
        """
        return AccountInformation(self.account_holder, self.balance)

    def deposit(self, amount: int) -> None:
        """
        Adds money to the balance of the account holder.
        :param amount: monetary value to add to the account
        """
        # Checks that the amount specified is valid
        self._check_valid(amount, "deposit")

        self.balance += amount

    def withdraw(self, amount: int) -> int:
        """
        Takes out a specified amount out of the balance.
        :param amount: The amount of money to take out
        :returns: The withdrawn amount
        """
        self._check_valid(amount, "withdraw")

        if self.balance - amount < 0:
            raise ValueError("The amount being withdrawn is more than the balance.")

        self.balance -= amount

        return amount

    @staticmethod
    def _check_valid(amount: int, action: str) -> None:
        """
        Checks if the amount of money positive and valid with the functions.
        :param amount: The amount to check
        :param action: The action that the account holder was trying to do. Should be ``deposit`` or ``withdraw``
        """
        # Checks that the amount specified is valid in general
        if amount < 0:
            raise ValueError(f"You cannot {action} a negative amount of money.")
        elif amount == 0:
            raise ValueError(f"You cannot {action} nothing.")
