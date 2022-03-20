"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers, power=2):
    """
    функция, которая принимает N целых чисел, и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    result = []
    for number in numbers:
        result.append(number ** power)

    return result


# filter types
INTEGER = "integer"
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_odd(number):
    return (number % 2) != 0


def is_even(number):
    return (number % 2) == 0


def is_prime(number):
    num = abs(number)
    if num == 1:
        result = True
    elif num > 2:
        result = True
        for i in range(2, number):
            if number % i == 0:
                result = False
    else:
        result = False

    return result


def filter_numbers(numbers, type=INTEGER):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers(range(1, 11), ODD)
    <<< [1, 3]
    >>> filter_numbers(range(1, 11), EVEN)
    <<< [2, 4]
    """
    result = []
    if type == "odd":
        for i in numbers:
            if is_odd(i):
                result.append(i)
    elif type == "even":
        for i in numbers:
            if is_even(i):
                result.append(i)
    elif type == "prime":
        for i in numbers:
            if is_prime(i):
                result.append(i)
    else:
        result = numbers

    return result


print('\n')
print("power_numbers are:", power_numbers(1, 2, 5, 7))

print('\n')
print("{} is {}".format(INTEGER, filter_numbers(range(1, 12))))
print("{} is {}".format(ODD, filter_numbers(range(1, 12), ODD)))
print("{} is {}".format(EVEN, filter_numbers(range(1, 12), EVEN)))
print("{} is {}".format(PRIME, filter_numbers(range(1, 12), PRIME)))

print('\n')
print("{} is {}".format(ODD, list(filter(is_odd, range(1, 12)))))
print("{} is {}".format(EVEN, list(filter(is_even, range(1, 12)))))
print("{} is {}".format(PRIME, list(filter(is_prime, range(1, 12)))))
