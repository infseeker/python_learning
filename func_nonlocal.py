def func_outer(a):
    x = a
    print('x равно', x)

    def func_inner():
        nonlocal x
        x *= 2

    func_inner()
    print('Локальное x сменилось на', x)


func_outer(5)
