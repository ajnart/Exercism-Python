class BankAccount:
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def open(self):
        self.__opened = True

    def deposit(self, amount):
        if self.__opened == False:
            raise ValueError("Account is closed")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if self.__opened == False:
            raise ValueError("Account is closed")
        else:
            self.__balance -= amount

    def close(self):
        self.__opened = False
