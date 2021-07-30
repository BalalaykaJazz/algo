from typing import List


def binary_search(store: List[int], x: int):
    """
    Реализация алгоритма двоичного поиска.
    store - отсортированная последовательность целых чисел.
    x - искомое целое число.

    Возвращаемое значение: индекс искомого числа или -1 в случае неудачи.
    """

    # left и right position - рассматриваемая часть последовательности,
    # в которой есть вероятность нахождения искомого числа.
    left_position = 0
    right_position = len(store) - 1

    while left_position <= right_position:

        # Средняя позиция в рассматриваемой части последовательности.
        median = int(left_position + (right_position - left_position) / 2)

        if store[median] == x:
            return median + 1
        elif store[median] > x:
            # Если найденное число больше искомого,
            # то отбросим правую часть последовательности
            # включая само найденное число.
            right_position = median - 1
        else:
            # аналогично с левой частью
            left_position = median + 1

    # возвращаем -1 в случае неудачи (если искомого числа нет в последовательности).
    return -1


def lower_bound(store: List[int], x: int) -> int:
    """Возвращет индекс самого левого вхождения искомого значения."""

    left_position = 0
    right_position = len(store) - 1

    while left_position <= right_position:

        median = int(left_position + (right_position - left_position) / 2)

        if store[median] >= x:
            right_position = median - 1
        else:
            left_position = median + 1

    if right_position + 1 < len(store) and store[right_position + 1] == x:
        return right_position + 1

    return -1


def upper_bound(store: List[int], x: int) -> int:
    """Возвращет индекс самого правого вхождения искомого значения."""

    left_position = 0
    right_position = len(store)

    while left_position < right_position:
        mid = int(right_position - (right_position - left_position) / 2)

        if x < store[mid]:
            right_position = mid
        else:
            left_position = mid + 1

    return left_position
