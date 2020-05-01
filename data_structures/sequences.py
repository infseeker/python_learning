shop_list = ['apples', 'mangoes', 'carrots', 'bananas']
name = 'Some String'

print(
    shop_list[0],
    shop_list[3],
    shop_list[-1],
    name[0],
    shop_list[:-1],
    name[:-1],
    name[-2],
    sep='\n'
)
print(type(set([1, 2, 3])))

# Ссылка на объект
print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist  # mylist - лишь ещё одно имя, указывающее на тот же объект!

del shoplist[0]  # Я сделал первую покупку, поэтому удаляю её из списка
print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что и shoplist, и mylist выводят один и тот же список
# без пункта "яблоко", подтверждая тем самым, что они указывают на один
# объект.

print('Копирование при помощи полной вырезки')
mylist = shoplist[:]  # создаём копию путём полной вырезки
del mylist[0]  # удаляем первый элемент

print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что теперь списки разные
