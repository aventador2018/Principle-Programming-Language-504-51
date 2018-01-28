class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.transactions = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions = self.transactions + 1

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions = self.transactions + 1

    def dump(self):
        s = '%s, %s, balance: %s' % \
            (self.name, self.no, self.balance)
        print s
        print 'Total number of transactions: %d' %(self.transactions)

account = Account('Zack', 111, 100)
account.deposit(20)
account.deposit(10)
account.withdraw(100)
account.dump()