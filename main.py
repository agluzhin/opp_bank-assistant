class Account:
    def __init__(self, number, balance, owner):
        self.__number = number
        self.__balance = balance
        self.__owner = owner

    def get_number(self):
        return self.__number

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    def set_number(self, number):
        self.__number = number

    def set_balance(self, balance):
        self.__balance = balance

    def set_owner(self, owner):
        self.__owner = owner


class Bank:
    def __init__(self):
        self.__accounts = []

    def add_account(self, account):
        self.__accounts.append(account)

    def delete_account(self, account):
        if account in self.__accounts:
            self.__accounts.remove(account)
            print('Account successfully removed.')
        else:
            print('Error... Incorrect account number is used.')

    def check_balance(self, number):
        for account in self.__accounts:
            if account.get_number() == number:
                return f'The owner of account with number {number} has {account.get_balance()}'
        return 'Error... Incorrect account number is used.'


account = Account(1298432, 1000000, 'Alex')
bank = Bank()

bank.add_account(account)
print(bank.check_balance(account.get_number()))
