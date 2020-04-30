x = 50


def func():
    global x
    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение x на', x)


func()
print('Значение x составляет', x)


def func_outer(a):
    x = a
    print('x равно', x)

    def func_inner():
        nonlocal x
        x *= 2

    func_inner()
    print('Локальное x сменилось на', x)


func_outer(5)
