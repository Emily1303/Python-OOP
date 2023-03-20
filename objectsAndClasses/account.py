class Account:

    def __init__(self, id: int, name: str, balance=0):
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return 'Сума надвишено салдо'

    def info(self):
        return f'Потребител {self.name} с акаунт {self.id} има {self.balance} баланс'


account1 = Account(13, 'Emily', 3000)
account1.credit(30)
account1.debit(20)
print(account1.info())