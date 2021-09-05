"""Пузырьковая сортировка. О(n^2)"""


def bubbleSort(nums: list[int]):
    """
    Осуществляется перебор по списку и сравнение соседних элементов.
    Если порядок не правильный, то они меняются местами.
    """

    swapped = True
    nums_size = len(nums)
    while swapped:
        swapped = False
        for i in range(nums_size - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


values = [5, 2, 1, 8, 4]
bubbleSort(values)
assert values == [1, 2, 4, 5, 8]
