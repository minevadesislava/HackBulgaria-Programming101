class BankAccount:

    
    def __init__(self, name, balance, currency):

        if balance < 0:
            raise ValueError("Start balance must be > 0.")
        if not isinstance(balance, int):
            raise TypeError

        self.name = str(name)
        self.balance = balance
        self.currency = currency
        self.account_history = ["Account was created!"]


    def history(self):
        return self.account_history

    def deposit(self, amount):
        self.balance += amount
        deposit_history = "Deposited {}{}".format(amount, self.currency)

    def balance_check(self):
        balance_history = "Balance check -> {}{}". format(self.balance, self.history)
        self.account_history.append(balance_history)
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            withdraw_history = "{}{} was withrdawed".format(amount, self.currency)
            self.account_history.append(withdraw_history)
            return True

        else:
            withdraw_history =" Withdraw for {}{} failed".format(amount, self.currency)
            self.account_history.append(withdraw_history)
            return False

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.balance, self.currency)

    def __int__(self):
        int_history = "Int check: {}{}".format(self.balance, self.currency)
        self.account_history.append(int_history)
        return self.balance

    def transfer_to(self, account, amount):
        if self.currency != account.currency:
            raise ValueError
        if self.balance < amount:
            return False
        account1 = 'Transfer to {} for {}{}'.format (account.name, amount, self.currency)
        account2 = 'Transer from {} for {}{}'.format(self.name, amount, account.currency)
        self.account_history.append(account1)
        account.account_history.append(account2)
        self.balance -= amount
        account.balance += amount
        return True

       
rado = BankAccount("Rado", 1000, "BGN")
ivo = BankAccount("Ivo", 0, "BGN")
print(rado.transfer_to(ivo, 500))
print(rado.balance_check())
print(ivo.balance_check())
print(rado.history())
print(ivo.history())
