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
