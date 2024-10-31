class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self._active = False
    
    def __str__(self):
        return f'Hello, {self.owner}. Your account balance is R${self.balance}'
    
    @classmethod
    def activate_account(cls, account):
        account._active = True

account1 = BankAccount('Daniela', 100)
account2 = BankAccount('Jimin', 1000000000)
print(account1)
print(account2)
account3 = BankAccount('RM', 10000000000)
print(f'Before activating: Is account active? {account3._active}')
BankAccount.activate_account(account3)
print(f'After activating: Is account active? {account3._active}')


class PythonicBankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance
        self._active = False

    @property
    def owner(self):
        return self._owner
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def active(self):
        return self._active