#модули
# 1 встроенные модули
# 2 собвственные модули
# 3 внешние
# venv - виртуальная среда
#
# import random
# random.Random()
#
# from random import *
# Random()

# внешние модули
# зависимости всё то что вы установили
# библиотека и фреймворк
from art import tprint
import colorama

print(colorama.Back.LIGHTMAGENTA_EX)
print(colorama.Fore.BLACK)
tprint('HELLO WORLD')
import random
print(random.randint(1,9))
