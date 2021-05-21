def division_func ():
    while True:
        val_1 = float(input('Введите делимое число: '))
        val_2 = float(input('Введите делитель числа: '))
        if val_2 == 0:
            print('Делить на ноль нельзя. Попробуйте ввести другое число.')
        else :
            val_div = val_1 / val_2
            return val_1, val_2, round(val_div, 2)
val_1, val_2, my_div = division_func()
print(f'Результат деления {val_1} на {val_2} равен {my_div}')