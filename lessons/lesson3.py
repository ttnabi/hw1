# байэль тут 3
# from lesson2 import Hum
# инкапсуляция -- капсула

# уровни доступа
# публичный
# защищенный - protected _
# private скрытый __  (_Class__atr) namemanling

# h=Hum('name')
# h.Hi()



class Person(object):
    def __init__(self, firsname, lastname, age, money):
        self.first = firsname
        self.last = lastname
        self._age = age
        self.__money = money

    def __str__(self):
        return self.first

    def _HI(self):
        print(f'Hi my name is {self.first} {self.last}\n'
              f'my old {self._age}')


    @property
    def money(self):
        print(self.__money)

    @money.deleter
    def money(self):
        self.__money = 0

    @money.setter
    def money(self, atr):
        self.__money = atr



first = Person('beka', 'qwerty', 20, 2020)
# first.first='Бека'
# first._age=10000
# first._Person__money=99

# first.HI()
first.money = 888
first.money


# first.age2=22
# print(first,first.age2)
# first.HI()
# first.kesh()
# f='erty'
# print(dir(first))
# print(dir(f))


class P2(Person):

    # def st(self):
    #     return super().__str__()

    def __str__(self):
        return f' hi {super().__str__()}'

# p=P2('first')
# print(p)
# print(p.st())




class Tea:
    def __init__(self,name):
        self.name=name

    def tea(self):
        print('поставь чай')
        self.__start()
        self.__control()
        self._stop()

    def __start(self):
        print('нагрев')

    def __control(self):
        print('контроль температуры')

    def _stop(self):
        print('выкл')


beko=Tea('beko')
beko.tea()
beko._stop