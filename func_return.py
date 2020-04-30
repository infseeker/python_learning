def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны.'
    else:
        return y


print(maximum(2, 3))


# return без указания возвращаемого значения эквивалентен выражению return None.
# Каждая функция содержит в неявной форме оператор return None в конце.

def some():
    pass


print(some())  # None
