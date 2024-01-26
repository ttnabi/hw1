# ООП
# class -все внутренности класса
# p = 'str', 1, 1.4, True, [], {}, (), None
# print(type(p))
#
def a(b, k):
    print(b + k)


# a(3,9)
# a(2,8)
# a(9,9)

#
class Human:
    # свойство класса
    head = '11'

    # магические методы
    # конструктор класса
    def __init__(self, name, age, nikname, abilka):
        self.name = name
        self.age = age
        self.nick = nikname
        self.power = abilka

    def __str__(self):
        return f'Nik: {self.nick}, Name: {self.name}, Ability: {self.power} {self.head}'

    def __len__(self):
        return len(self.power)

    # метод
    def Hi(self):
        print(self.age * 2)


# p2='SDRTGHJIJHN'
# o='drfgh'
# print(p2.join('fdgh'))
# экземпляр/обьект класса
hum = Human('beka', 20, 'T9', 'писать стихи')
hum2 = Human('Ибрагим', 14, 'kuizee', 'играть')
hum3 = Human('Руслан', 16, 'RAWE', 'ИГРАТЬ на гитаре')

hum2.RT = 'Расширение терретории'
hum2.power='fghj'
hum.age = 10
print(hum.age)
print(hum2.RT)
hum.Hi()
hum3.

class Human2:
    def __init__(self, name, age, nikname, abilka):
        self.name = name
        self.age = age
        self.nick = nikname
        self.power = abilka

    def hello(self):
        self.name = 'edrty'


Human2.hello(hum)
print(hum)

from beka import beka1
# git, github gitlub bitbaket