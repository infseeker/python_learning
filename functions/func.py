if __name__ == '__main__':
    print('Hello!')


def say_hello(text='Hello, World!'):
    print(text)  # блок, принадлежащий функции


if __name__ == '__main__':
    # Конец функции
    say_hello("Hello")  # вызов функции
    say_hello()  # ещё один вызов функции
