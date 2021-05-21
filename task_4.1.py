# Задание 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.

## Исходная задача: В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
## Немного преобразуем задачу для работы c функцией:

import timeit

import cProfile

import random

def replace(SIZE):
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    max_el = 0
    min_el = 0
    for i in range(SIZE):
        if array[i] > array[max_el]:
            max_el = i
        elif array[i] < array[min_el]:
            min_el = i
    array[max_el], array[min_el] = array[min_el], array[max_el]
    return array

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
print(replace(SIZE))

## Проанализируем функцию по timeit:

print(timeit.timeit('replace(5)', number=1000, globals=globals())) #0.009453294000000056
print(timeit.timeit('replace(10)', number=1000, globals=globals())) #0.015679302999999978
print(timeit.timeit('replace(15)', number=1000, globals=globals())) #0.022870797000000054
print(timeit.timeit('replace(20)', number=1000, globals=globals())) #0.029584031000000066
print(timeit.timeit('replace(25)', number=1000, globals=globals())) #0.036707191999999944
print(timeit.timeit('replace(30)', number=1000, globals=globals())) #0.0432678700000001

## Проанализируем функцию по cProfile:

cProfile.run('replace(1_000)')
#5260 function calls in 0.003 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.000    0.000    0.003    0.003 main.py:1144(replace)
#         1    0.000    0.000    0.002    0.002 main.py:1145(<listcomp>)
#      1000    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
#      1000    0.001    0.000    0.002    0.000 random.py:290(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:334(randint)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1255    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

## Eсли не брать в расчет вызов random, которые можно вынести за функцию, процессы производятся 1 раз, а число timeit 
## увеличивается в зависимости от количества операций. Сложность O(log n).
## Преобразуем функцию с помощью встроенных функций max и min:

def replace_short(SIZE):
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    max_el = array.index(max(array))
    min_el = array.index(min(array))
    array[max_el], array[min_el] = array[min_el], array[max_el]
    return array


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

print(replace_short(SIZE))

## Проанализируем функцию по timeit:
print(timeit.timeit('replace_short(5)', number=1000, globals=globals())) #0.009003647000000004
print(timeit.timeit('replace_short(10)', number=1000, globals=globals())) #0.015112793
print(timeit.timeit('replace_short(15)', number=1000, globals=globals())) #0.021352668000000005
print(timeit.timeit('replace_short(20)', number=1000, globals=globals())) #0.02792492499999999
print(timeit.timeit('replace_short(25)', number=1000, globals=globals())) #0.034817452
print(timeit.timeit('replace_short(30)', number=1000, globals=globals())) #0.04061725800000002

## Проанализируем функцию по cProfile:

cProfile.run('replace_short(1_000)')
#5282 function calls in 0.002 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.000    0.000    0.002    0.002 main.py:1230(replace_short)
#         1    0.000    0.000    0.002    0.002 main.py:1231(<listcomp>)
#      1000    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
#      1000    0.001    0.000    0.001    0.000 random.py:290(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:334(randint)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1273    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

## Напишем более длинную реализацию:

def replace_long(SIZE):
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    max_el = 0
    for i in range(SIZE):
        f = True
        for j in range(SIZE):
            if array[i] < array[j] and i != j:
                f = False
                break
        if f:
            max_el = i
            break
    min_el = 0
    for i in range(SIZE):
        f = True
        for j in range(SIZE):
            if array[i] > array[j] and i != j:
                f = False
                break
        if f:
            min_el = i
            break
    array[max_el], array[min_el] = array[min_el], array[max_el]
    return array


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

print(replace_long(SIZE))

## Проанализируем функцию по timeit:
print(timeit.timeit('replace_long(5)', number=1000, globals=globals())) #0.014071331000000003
print(timeit.timeit('replace_long(10)', number=1000, globals=globals())) #0.024158973
print(timeit.timeit('replace_long(15)', number=1000, globals=globals())) #0.03474333200000001
print(timeit.timeit('replace_long(20)', number=1000, globals=globals())) #0.04611375200000001
print(timeit.timeit('replace_long(25)', number=1000, globals=globals())) #0.05695735499999999
print(timeit.timeit('replace_long(30)', number=1000, globals=globals())) #0.06601042400000001

## Проанализируем функцию по cProfile:

cProfile.run('replace_long(1_000)')
# 5264 function calls in 0.003 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.001    0.001    0.003    0.003 main.py:1197(replace_long)
#         1    0.000    0.000    0.002    0.002 main.py:1198(<listcomp>)
#      1000    0.001    0.000    0.001    0.000 random.py:237(_randbelow_with_getrandbits)
#      1000    0.001    0.000    0.002    0.000 random.py:290(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:334(randint)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1259    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

## Вывод: наиболее эффективной является функция replace_short за счет встроенных функций - 0,002 секунды в сProfile был наименьшим результатом.
