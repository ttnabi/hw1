# множественное наследование
# venv - модули библиотеки зависимости фреймворки пакеты

# модуль 3   #библиотека
# встроенный
from random import *

from random import randint
# from math import *
# print(nan)
#
# import math
# print(math.nan)


#2 собвственные модули

from lesson3 import Tea
import lesson3
lesson3.Human
n=Tea('ego')
n.tea()

#3 внешние модули
# venv - виртуальная среда\ для скачивания модулей



#
# class A:
#     def __init__(self, b, c, d):
#         self._b = b
#         self._c = c
#         self._d = d
#
#     # def get_point(self):
#     #     print(self._d, self._c, self._b)
#     #
#     # def set_point(self, b, c, d):
#     #     self._b = b
#     #     self._c = c
#     #     self._d = d
#
#     @property
#     # getter
#     def point(self):
#         return f'{self._b},{self._c},{self._d}'
#
#     @point.setter
#     def point(self, b):
#         self._b = b
#
#
#     @point.deleter
#     def point(self):
#         del self._b
#
#
#
# # a = A('b', 'c', 14)
# #
# # a.point=1
# # # print(a.point)
# # del a.point
# # a.point = 0
# # print(a.point)
#
# # a.get_point()
# # a.set_point('B','C','D')
# # a.get_point()
#
#
# class Hum:  # родительский\супер класс
#     def __init__(self,name1):
#         self.name1=name1
#
#     def run(self):
#         print(self.name1,'run')
#
# hum1=Hum('albus')
# hum1.run()
#
#
# class Hum3(Hum):...
#
# class SuperHum: # родительский\супер класс
#     def __init__(self,name,superpower):
#         self.name=name
#         self.power=superpower
#
#
#     def run(self):
#         print(self.power)
#
#
# c=SuperHum('Albus','Mage')
# c.run()
#
#
# class Hum2(SuperHum,Hum3,Hum):
#     def __init__(self,name,superpower,name1):
#         SuperHum.__init__(self,name,superpower)
#         Hum.__init__(self,name1)
#
#     def run(self):
#         Hum.run(self)
#         SuperHum.run(self)
#
# h=Hum2('name','super','name1')
#
# h.run()
#
# # MRO-method resolution order
# print(Hum2.mro())
# h.run()
