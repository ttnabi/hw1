class SavingAccount:
    pass

class CheckingAccount:
    pass


class RealEstate:
    pass


class Bond:
    pass


class Stock:
    pass


class Security(Bond, Stock):
    pass


class BankAccount(CheckingAccount, SavingAccount):
    pass


class Insurableltem(BankAccount, RealEstate):
    pass


class Assest(RealEstate, BankAccount, Security):
    pass


class InterestBearingItem(BankAccount, Security):
    pass
