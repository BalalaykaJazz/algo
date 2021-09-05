"""Сортировка подсчетом. O(n + k)"""


def countSort(nums: list[int]):
    """
    Подсчитываем, сколько раз в массиве встречается каждое значение,
    и заполняем массив подсчитанными элементами в соответствующих количествах.
    """

    if not nums:
        return
    num_count = [0] * (1 + max(nums))
    for x in nums:
        num_count[x] += 1
    i = 0
    for j in range(len(nums)):
        while num_count[i] == 0:
            i += 1
        nums[j] = i
        num_count[i] -= 1


values = [5, 2, 1, 8, 4]
countSort(values)
assert values == [1, 2, 4, 5, 8]
