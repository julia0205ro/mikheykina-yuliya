"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args: int) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

    return list(map(lambda x: x ** 2, args))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number: int) -> bool:
    """
    функция, которая принимает одно целое число
    и возвращает  True если это число простое,
    False если число составное
    """

    if number <= 1:
        return False

    for digit in range(2, number):
        if number % digit == 0:
            return False

    return True


def filter_numbers(digit_list: list[int], filter_type: str) -> list[int]:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type == ODD:
        return list(filter(lambda x: x % 2 == 1, digit_list))
    elif filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, digit_list))
    else:
        return list(filter(is_prime, digit_list))


# проверка кода
if __name__ == '__main__':
    print(power_numbers(1, 2, 5, 7))
    print(is_prime(13))
    print(filter_numbers([1, 2, 3], ODD))
    print(filter_numbers([2, 3, 4, 5], EVEN))
    print(filter_numbers([2, 3, 4, 5], PRIME))
