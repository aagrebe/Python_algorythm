# Задание 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

def summa(i, n, k, sum_n):
    if i == n:
        return sum_n
    else:
        sum_n += sum_n * 0.5**i * k
        i += 1
        k *= -1
        return summa(i, n, k, sum_n)


i = 1
k = -1
sum_n = 1
n = int(input('Введите количество элементов ряда чисел: 1 -0.5 0.25 -0.125... : '))
print(summa(i, n, k, sum_n))