def sum_func(numbers_replace):
    global all_sum
    numbers_sum = sum(map(float, numbers_replace))
    all_sum += numbers_sum
    return all_sum

def sum_exit_func(numbers):
    global all_sum, x
    numbers_replace = list(numbers.split(' '))
    for i in range(len(numbers_replace)):
        if numbers_replace[i] == 'q':
            numbers_replace_q = numbers_replace[:i]
            all_sum = (sum_func(numbers_replace_q))
            x = 1
            return all_sum, x
    all_sum = (sum_func(numbers_replace))
    return all_sum, x


all_sum = 0
x = 0
while True:
    numbers = input('Введите строку чисел через пробел, для получения суммы чисел нажмите "Enter, для выхода нажмите "q": ')
    numbers_sum = sum_exit_func(numbers)
    print(f'Сумма чисел равна {all_sum}')
    if x == 1:
        break