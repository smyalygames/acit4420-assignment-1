from bank.bank import BankAccount


class CheckingAccount(BankAccount):
    def __init__(self, name: str, fee: int):
        """
        A bank account that has fees per withdrawal.
        :param name: Name of the account holder
        :param fee: Fixed fee for withdrawals
        """
        super().__init__(name)

        if fee < 0:
            raise ValueError("The fee cannot be negative.")

        self.fee = fee

    def withdraw(self, amount: int) -> int:
        """
        Withdraws the amount specified from the account, with the additional fee.
        :param: The amount to withdraw, excludes the fee
        """
        super().withdraw(amount + self.fee)

        return amount
