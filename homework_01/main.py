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
    print(f'\tnumbers are {numbers}\n')
    result = []
    for number in numbers:
        result.append(number ** power)

    return result


# constants
my_list = range(1, 12)

# filter types
INTEGER = "integer"
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_integer(number):
    return type(number) is int


def is_odd(number):
    return (number % 2) != 0


def is_even(number):
    return (number % 2) == 0


def is_prime(number):
    num = abs(number)
    if num > 1:
        result = True
        for i in range(2, number):
            if number % i == 0:
                result = False
    else:
        result = False

    return result


def filter_numbers(numbers, filter_type=INTEGER):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers(range(1, 11),ODD)
    <<< [1, 3]
    >>> filter_numbers(range(1, 11),EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        result = list(filter(is_odd, numbers))
    elif filter_type == EVEN:
        result = list(filter(is_even, numbers))
    elif filter_type == PRIME:
        result = list(filter(is_prime, numbers))
    else:
        result = list(numbers)

    return result


print('\nФункция, которая принимает N целых чисел и возвращает список квадратов этих чисел')
print("\tpower_numbers are:", power_numbers(1, 2, 5, 7))

print('\nФункция, которая на вход принимает список из целых чисел,'
      ' и возвращает только чётные/нечётные/простые числа (вариант решения №1)')
print("\t{} input is \t{}\n".format(INTEGER, filter_numbers(my_list, INTEGER)))
print("\t{} result is \t\t{}".format(ODD, filter_numbers(my_list, ODD)))
print("\t{} result is \t\t{}".format(EVEN, filter_numbers(my_list, EVEN)))
print("\t{} result is \t{}".format(PRIME, filter_numbers(my_list, PRIME)))

print('\nФункция, которая на вход принимает список из целых чисел,'
      ' и возвращает только чётные/нечётные/простые числа (вариант решения №2)')
print("\t{} input is \t{}\n".format(INTEGER, list(filter(is_integer, my_list))))
print("\t{} result is \t\t{}".format(ODD, list(filter(is_odd, my_list))))
print("\t{} result is \t\t{}".format(EVEN, list(filter(is_even, my_list))))
print("\t{} result is \t{}".format(PRIME, list(filter(is_prime, my_list))))
