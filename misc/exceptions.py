try:
    text = input('Введите что-нибудь --> ')
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except KeyboardInterrupt:
    print('Вы отменили операцию.')
else:
    # Выполняется, если нет исключений
    print('Вы ввели {0}'.format(text))
finally:
    # Выполняется всегда.
    # Выполнется перед return, если он есть.
    print('Finally')
