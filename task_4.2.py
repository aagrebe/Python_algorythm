# Задание 2. Написать два алгоритма нахождения i-го по счёту простого числа.
#Используя алгоритм «Решето Эратосфена»
#Без использования «Решета Эратосфена»

import timeit

import cProfile

def eratosthenes(num_index):
    array = [_ for _ in range(2, num_index * 6 + 1)]  # проверяла, считает до 189
    # потом только если буду увеличивать коэф., но не нашла универсальной функции, ищу долго
    # везде пишут только про другие подходы к этой задаче
    num = 2
    i = 0

    while num < array[-1]:
        while len(array) > i:
            if array[i] % num == 0 and array[i] != num:
                array.pop(i)
            i += 1
        i = 0
        for j in range(len(array)):
            if array[j] > num:
                num = array[j]
                break
    for el in range(len(array)):
        if el == num_index - 1:
            return array[el]


## Проанализируем функцию по timeit:

print(timeit.timeit('eratosthenes(5)', number=1000, globals=globals()))  # 0.036177064999999994
print(timeit.timeit('eratosthenes(10)', number=1000, globals=globals()))  # 0.078041173
print(timeit.timeit('eratosthenes(15)', number=1000, globals=globals()))  # 0.14341328000000003
print(timeit.timeit('eratosthenes(20)', number=1000, globals=globals()))  # 0.20181239899999998
print(timeit.timeit('eratosthenes(25)', number=1000, globals=globals()))  # 0.27292471900000004
print(timeit.timeit('eratosthenes(30)', number=1000, globals=globals()))  # 0.35956434699999995

## Проанализируем функцию по cProfile:

cProfile.run('eratosthenes(100)')
# 12887 function calls in 0.005 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.004    0.004    0.005    0.005 main.py:1174(eratosthenes)
#         1    0.000    0.000    0.000    0.000 main.py:1175(<listcomp>)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#     12392    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       490    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}

def no_eratosthenes(num_index):
    array = []
    for i in range(2, num_index * 6 + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            array.append(i)

    for el in range(len(array)):
        if el == num_index - 1:
            return array[el]


## Проанализируем функцию по timeit:

print(timeit.timeit('no_eratosthenes(5)', number=1000, globals=globals()))  # 0.016263728000000005
print(timeit.timeit('no_eratosthenes(10)', number=1000, globals=globals()))  # 0.03943763
print(timeit.timeit('no_eratosthenes(15)', number=1000, globals=globals()))  # 0.07581058800000001
print(timeit.timeit('no_eratosthenes(20)', number=1000, globals=globals()))  # 0.11937100900000003
print(timeit.timeit('no_eratosthenes(25)', number=1000, globals=globals()))  # 0.166376099
print(timeit.timeit('no_eratosthenes(30)', number=1000, globals=globals()))  # 0.22796509499999995

## Проанализируем функцию по cProfile:

cProfile.run('no_eratosthenes(100)')
# 114 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 main.py:1203(no_eratosthenes)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       109    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

## Очевидно, что вторая функция быстрее как по timeit, так и cProfile + компактнее в плане кода.
## Квадратичная сложность О(n2).