from bank.bank import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, name: str, interest_rate: float):
        """
        A savings account with an interest rate.
        :param name: Name of the account holder
        :param interest_rate: The interest rate as a percentage in decimal form. e.g. 2% interest is 0.02
        """
        super().__init__(name)

        self._check_valid(interest_rate, "interest rate")

        self.interest_rate = interest_rate

    def apply_interest(self) -> int:
        """
        Applies the account's interest rate on the account's balance.
        :returns: The amount of interest gained.
        """
        # If there is no interest to be applied.
        if self.balance == 0:
            return 0

        # Calculate the amount of interest to be gained.
        # The amount is rounded to the nearest integer to make it fair.
        interest = round(self.balance * self.interest_rate)
        # Add the interest to the balance
        self.deposit(interest)

        return interest
