class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points,
                 catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def print_name(self):
        print(self.name)

    def multiply_health(self):
        self.health_points *= 2

    def __str__(self):
        return (f"Прозвище: {self.nickname}, "
                f"Суперспособность: {self.superpower},"
                f"Здоровье: {self.health_points}")

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Супермен", "Человек из стали", "Летание и суперсила", 150, "Я последний сын Криптона!")

hero.print_name()
hero.multiply_health()
print(hero)
print(len(hero))


class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def print_name(self):
        print(self.name)

    def multiply_health(self):
        self.health_points *= 2

    def __str__(self):
        return (f"Nickname: {self.nickname}, "
                f"Superpower: {self.superpower}, "
                f"Health Points: {self.health_points}")

    def __len__(self):
        print("len_catchphrase: ", len(self.catchphrase))


hero = SuperHero("Superman", "Man of Steel", "Flying and Superpower", 150, "I am the last son of Krypton!")

print(hero.__str__())
hero.multiply_health()
hero.__len__()


class AquaWoman(SuperHero):
    tail = "fish-like"

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
        self.damage = damage

    def print_health(self):
        self.fly = False
        print(f'health: {self.health_points ** 2}')

    def get_info(self):
        print('True in the True_phrase')


aqua_woman = AquaWoman(name="Mera", nickname="Queen of the Sea", superpower="Hydrokinesis", health_points=80,
                       catchphrase="The tide is turning!", damage=15, fly=False)
print(aqua_woman.__str__())
aqua_woman.print_health()
print(aqua_woman.__len__())


class FireMan(SuperHero):
    hose = "extendable"

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
        self.damage = damage

    def print_health(self):
        print(f'Health: {self.health_points ** 2}')

    def get_info(self):
        print('True in the True_phrase')


fire_man = FireMan(name="John", nickname="The Firefighter", superpower="Fire Manipulation", health_points=100,
                   catchphrase="I'll put that fire out!", damage=20, fly=False)
print(fire_man.__str__())
fire_man.print_health()
print(fire_man.__len__())


class FireVillain(FireMan):
    people = "monster"

    def gen_x(self):
        pass

    def crit(self, damage):
        print(f'damage: {damage ** 2}')


fire_villain = FireVillain(name="Molotov", nickname="The Arsonist", superpower="Fire Manipulation", health_points=100,
                           catchphrase="Burn, baby, burn!", damage=20, fly=False)
print(fire_villain.__str__())
fire_villain.gen_x()
fire_villain.crit(fire_man.damage)
