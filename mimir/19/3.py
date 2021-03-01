class Account:
    def __init__(self,balance: float,interest_rate:float) -> None:
        self.__balance = balance
        self.__interest_rate = interest_rate
    def update_balance(self):
        self.__balance *= (1 + self.__interest_rate / 100)

    def __str__(self) -> str:
        return f"Balance: {self.__balance:.2f}"


class SavingsAccount(Account):
    INTEREST_RATE = 5.0
    BONUS_RATE = 10.0

    def __init__(self,balance:float) -> None:
        super().__init__(balance,SavingsAccount.INTEREST_RATE+SavingsAccount.BONUS_RATE)


class DebitAccount(Account):
    INTEREST_RATE = 2.0

    def __init__(self,balance:float) -> None:
        super().__init__(balance,DebitAccount.INTEREST_RATE)

def print_accounts(accounts):
    for account in accounts:
        print(account)
    print()

def update_accounts(accounts):
    for account in accounts:
        account.update_balance()

sav1 = SavingsAccount(1000)
deb1 = DebitAccount(1000)
sav2 = SavingsAccount(2000)
deb2 = DebitAccount(4000)

accounts = [sav1, deb1, sav2, deb2]
print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)
update_accounts(accounts)

print_accounts(accounts)