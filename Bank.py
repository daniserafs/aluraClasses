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

account4 = PythonicBankAccount('Jin', 999000000000)
print(f'Owner of account number 4: {account4.owner}')

class BankClient:
    def __init__(self, name, age, adress, cpf, profession):
        self.name = name
        self.age = age
        self.adress = adress
        self.cpf = cpf
        self.profession = profession

    @classmethod
    def create_account(cls, owner, initial_balance):
        account = PythonicBankAccount(owner, initial_balance)
        return account

    def __str__(self) -> str:
        return f'{self.name} | {self.age} | {self.adress} | {self.cpf} | {self.profession}'

client1 = BankClient('Julieta', 20, 'A Street', '745.014.360-77', 'Backend')
client2 = BankClient('Julio', 25, 'B Street', '971.091.030-21', 'Frontend')
client3 = BankClient('Julia', 19, 'C Street', '717.997.600-81', 'Student')

account_client1 = BankClient.create_account('Ana', 2000)
print(f'{account_client1.owner} account was created with initial balance of R${account_client1.balance}')

print(client1)
print(client2)
print(client3)