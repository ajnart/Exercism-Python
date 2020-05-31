class BankAccount:
    def __init__(self):
        self.__opened = None
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def open(self):
        if self.__opened == False:
            raise ValueError("Account can't be opened twice")
        else:
            self.__opened = True

    def deposit(self, amount):
        if self.__opened == False or amount < 0:
            raise ValueError("Account is closed")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if self.__opened == False or amount > self.__balance:
            raise ValueError("Account is closed")
        else:
            self.__balance -= amount

    def close(self):
        if self.__opened == False:
            raise ValueError("Account not open")
        else:
            self.__opened = False
            self.__balance = 0
