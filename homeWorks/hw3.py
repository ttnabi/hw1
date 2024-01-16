class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        user = int(input('Введите сумму которую нужно добавить: '))
        if 0 < user:
            self._balance += user
            print(f"Теперь ваш баланс: {self._balance}")
        else:
            print("Вы ввели недопустимое число")

    def _kill(self):
        self._balance = 0
        print(f"Вы обнулили свой баланс {self._balance}")

    def __jackpot(self):
        self._balance *= 10
        print(f"Поздравляю вы получили джекпот {self._balance}")

    def _join(self, other):
        self._balance += other._balance

