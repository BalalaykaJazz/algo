"""
Быстрая сортировка. В худшем случае O(n^2), если опорный элемент равен наименьшему или наибольшему.
В остальных случаях O(n log n)."""


def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quickSort(nums: list[int]):
    """
    Все элементы меньше опорного перемешаются слева от него, остальные — справа.
    Действие выполняется рекурсивно.
    """

    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


values = [5, 2, 1, 8, 4]
quickSort(values)
assert values == [1, 2, 4, 5, 8]
