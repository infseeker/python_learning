import os
import time

# Указываем пути к папкам для создания бэкапа
source = ['/home/infseek/Documents/WebDev', '/home/infseek/Documents/Sea']

# Указываем пути к папке, куда будут сохраняться бэкапы
target_dir = '/home/infseek/Documents/Backup'

# Текущая дата - имя папки с архивами за текущую дату
today = target_dir + os.sep + time.strftime('%Y-%m-%d')
# Текущее время - имя zip-архива
now = time.strftime('%H:%M:%S')

# Создаём каталог, если его нет
if not os.path.exists(today):
    os.mkdir(today)
    print('The folder was created successfully')

# Имя zip-файла
target = today + os.sep + now + '.zip'

# Текстовая команда zip операционной системы для создания архива
zip_command = f'zip -qr {target} {" ".join(source)}'

# Запуск программы и проверка результата
if os.system(zip_command) == 0:
    print('Backup was created in', target)
else:
    print('Operation failed')
