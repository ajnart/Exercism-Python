class BankAccount:
    def __init__(self):
        self.__opened = None
        self.__balance = 0

    def get_balance(self):
        if self.__opened == False:
            raise ValueError("Account is closed.")
        else:
            return self.__balance

    def open(self):
        if self.__opened:
            raise ValueError("Account can't be opened twice")
        else:
            self.__opened = True

    def deposit(self, amount):
        if self.__opened == False or amount < 0:
            raise ValueError("Account is closed")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if not self.__opened or amount > self.__balance or amount < 0:
            raise ValueError("Account is closed / can't withdraw that much / can't withdraw a negative value, silly!")
        else:
            self.__balance -= amount

    def close(self):
        if not self.__opened:
            raise ValueError("Account not open")
        else:
            self.__opened = False
            self.__balance = 0
