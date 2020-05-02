class Person:
    population = 0

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hi! My name is', self.name)

    # Метод, вызываемый при уничтожении объекта
    def __del__(self):
        """I'm dying"""
        print(f'{self.name} is destroying')


p = Person('R2D2')
p.say_hi()
# Можно напрямую уничтожить объект
del p
