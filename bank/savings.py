from bank.bank import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, name: str, interest_rate: float):
        """
        A savings account with an interest rate.
        :param name: Name of the account holder
        :param interest_rate: The interest rate as a percentage in decimal form. e.g. 2% interest is 0.02
        """
        super().__init__(name)

        if interest_rate <= 0:
            raise ValueError("Interest rate has to be positive.")

        self.interest_rate = interest_rate

    def apply_interest(self) -> float:
        """
        Applies the account's interest rate on the account's balance.
        :returns: The amount of interest gained.
        """
        # Calculate the amount of interest to be gained
        interest = self.balance * self.interest_rate
        # Add the interest to the balance
        self.balance += interest

        return interest
