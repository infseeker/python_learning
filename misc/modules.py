import sys
import functions.func as f

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)
print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')

f.say_hello()
f.say_hello('From module')
