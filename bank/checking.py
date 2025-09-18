from bank.bank import BankAccount


class CheckingAccount(BankAccount):
    def __init__(self, name: str, transaction_fee: int):
        """
        A bank account that has fees per withdrawal.
        :param name: Name of the account holder
        :param transaction_fee: Fixed fee for withdrawals
        """
        super().__init__(name)

        if transaction_fee < 0:
            raise ValueError("The fee cannot be negative.")

        self.transaction_fee = transaction_fee

    def withdraw(self, amount: int) -> int:
        """
        Withdraws the amount specified from the account, with the additional fee.
        :param: The amount to withdraw, excludes the fee
        :returns: The withdrawn amount (without the fees)
        """
        super().withdraw(amount + self.transaction_fee)

        return amount
