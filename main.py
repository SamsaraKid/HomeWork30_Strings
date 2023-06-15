lirycscats = '''
Кошки не похожи на людей,
Кошки - это кошки.
Люди носят шляпы и пальто,
Кошки часто ходят без одежки.
Кошки могут среди бела дня
Полежать спокойно у огня,
Кошки не болтают чепухи,
Hе играют в домино и шашки,
Hе обязаны писать стихи,
Им плевать на разные бумажки.
Людям не сойти с протоптанной дорожки,
Hу, а кошки - это кошки.
'''

print('Песня про кошек\n', lirycscats)

numcats = lirycscats.lower().count('кошки') + lirycscats.lower().count('кошка')

print('Кошек в песне:', numcats)

lirycsmouse = lirycscats.replace('Кошки', 'Мышки').replace('Кошка', 'Мышка').replace('кошки', 'мышки').replace('кошка', 'мышка')

print('\nПесня про мышек\n', lirycsmouse)


login = input('Введите логин:\n')
passw = ''
while True:
    passw = input('Введите пароль:\n')
    if len(passw) < 8:
        print('Пароль должен состоять минимум из 8 символов')
    elif passw.isalpha():
        print('Пароль должен содержать цифры')
    elif passw.isdigit():
        print('Пароль должен содержать буквы')
    else:
        break
while True:
    passw1 = input('Повторите пароль:\n')
    if passw1 != passw:
        print('Пароль не совпадает')
    else:
        break


