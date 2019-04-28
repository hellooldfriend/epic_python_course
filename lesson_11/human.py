#Создайте тип данных Human, определите атрибуты и методы для работы с ним.

#Человек ест, спит, ходит на работу и отдыхает на протяжении 70 лет.
# С 18 лет человек начинает работать и в 65 лет выходит на пенсию.



class Human:
    def __init__(self, name=''):
        self.name = name
        self.age = 0

        print(f'Родился человек с именем {self.name}')
        print(f'{self.name} отмечает день рождения')

    def eating(self):
        print(f'{self.name} ест')

    def sleeping(self):
        print(f'{self.name} спит')

    def working(self):
        if self.age >= 18 and self.age < 60:
            print(f'{self.name} работает')
        elif self.age >= 60:
            print(f'{self.name} на пенсии')

    def relaxing(self):
        print(f'{self.name} отдыхает')

    def growing(self):
        self.age += 1
        print(f'{self.name} отмечает день рождения')

class Life:
    def life(self, human, years=70):
        while years:
            human.growing()
            human.eating()
            human.sleeping()
            human.working()
            human.relaxing()
            years -= 1

petr = Human('Петр')
life_petr = Life()
life_petr.life(petr)


