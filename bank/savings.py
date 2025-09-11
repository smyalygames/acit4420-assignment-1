from bank.bank import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, name: str, interest_rate: float):
        """
        A savings account with an interest rate.
        :param name: Name of the account holder
        :param interest_rate: The interest rate as a percentage in decimal form. e.g. 2% interest is 0.02
        """
        super().__init__(name)

        # TODO maybe add a check if the interest rate is valid? i.e. not negative.

        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        """
        Applies the account's interest rate on the account's balance.
        """
        self.balance = self.balance * (1 + self.interest_rate)
