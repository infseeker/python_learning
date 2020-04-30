def total(a=5, *numbers, **phonebook):
    # *numbers (*args) - параметры
    # **phonebook (**kwargs)- ключевые параметры
    print('a', a)
    # проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)
    # проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560)


# Keywords only
def total_1(initial=5, *numbers, extra_number=10):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)


total_1(10, 1, 2, 3, extra_number=50)
total_1(10, 1, 2, 3)
# Вызовет ошибку, поскольку мы не указали значение
# аргумента по умолчанию для 'extra_number'.
