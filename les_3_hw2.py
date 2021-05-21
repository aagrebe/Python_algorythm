def info (name, surname, year, city, mail, mobile):
        print(f'Карточка пользователя: имя - {name}, фамилия - {surname}, год рождения - {year}, город проживания - {city}, e-mail - {mail}, телефон - {mobile}')

print('Заполните карточку пользователя')
my_name = input('Имя: ')
my_surname = input('Фамилия: ')
my_year = int(input('Год рождения: '))
my_city = input('Город проживания: ')
while True:
    my_mail = input('Электронная почта: ')
    if my_mail.find('@') == -1:
        print('Вы ввели электронную почту некорректно, проверьте наличие @')
    else:
        break
my_mobile = int(input('Телефон (пример - 81110001100: '))
my_info = info(name = my_name, surname = my_surname, year = my_year, city = my_city, mail = my_mail, mobile = my_mobile)