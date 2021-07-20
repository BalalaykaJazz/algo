
def binary_search(store: list, x: int):
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
            return median
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
