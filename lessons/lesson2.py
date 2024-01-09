# ООП Наследование полиморфизм
# Инкапсуляцию
#
class Hum(object):  # супер класс - родительский класс
    # магический метод
    def __init__(self, name):
        self.name = name
        # self.age=age

    # метод
    def Hi(self): ...

    def __str__(self):
        return 'HI'

    def __len__(self):
        return len(self)


# экземпляр\обьект
h = Hum('sdfg')
h.name = 'beka'
h.Hi()


class Student(Hum):  # дочерний класс
    # def __

    def Hi(self):
        print('Hello ', self.name)


student = Student('beka')
student.Hi()

print(Student.mro())


class Kid(Student):
    def __init__(self, name, age, lastname):
        # super().__init__(name)
        Student.__init__(self, name)
        self.age = age
        self.last = lastname

    def Hi(self):
        Hum.Hi(self)


c = Kid('Beka', 14, 'DZU')

c.Hi()


class Kid2(Kid):
    def __init__(self, name, age, lastname, fly=False):
        super().__init__(name, age, lastname)
        self.fly = fly

    def __str__(self):
        return f"{super().__str__()}, " \
               f"name: {self.name}, age: {self.age}," \
               f" latname: {self.last}, can fly: {self.fly}"


kid = Kid2('beka', 11, 'wer', False)

print(kid)

