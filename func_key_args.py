def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)


func(3, 7)
func(25, c=24)  # ключевой параметр c
func(c=50, a=100)  # ключевые параметры c и a