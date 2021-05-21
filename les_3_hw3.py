def sum_max (val_1, val_2, val_3):
    val = [val_1, val_2, val_3]
    val_min = min(val)
    val.remove(val_min)
    val_sum = sum(val)
    return val_sum
val_1 = float(input('Введите первое число: '))
val_2 = float(input('Введите второе число: '))
val_3 = float(input('Введите третье число: '))
my_sum_max = sum_max(val_1, val_2, val_3)
print(f'Сумма наибольших двух чисел равна: {my_sum_max}')