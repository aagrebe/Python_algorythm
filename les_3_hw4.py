def my_func(x, y):
    degree = x ** y
    return degree

def my_func_2 (x, y):
    if y == 0: return 1
    result = x
    for index in range(abs(y) - 1):
        result *= x
        index += 1
    return 1 / result
x = float(input('Введите действительное число x: '))
y = int(input('Введите целое число y: '))
if y > 0 : y = y * -1
print(f'Число x : {x}, число y : {y}')
print(f'Результат первого вычисления с помощью оператора ** : {my_func(x, y)}')
print(f'Результат второго вычисления с помощью цикла : {my_func_2(x, y)}')