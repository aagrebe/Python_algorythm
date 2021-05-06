# Задание 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более
# чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.


import random


def guess(i, l):
    i += 1
    if i <= 10:
        r = int(input(f'Угадайте число от 0 до 100: '))
        if r == l:
            return f'Поздравляю! Вы угалали, это число {l}'
        else:
            print(f'У вас осталось {10 - i} попыток')
            return guess(i, l)
    else:
        return f'Вы проиграли :( это число {l}'


i = 0
l = random.randint(0, 100)
print(guess(i, l))