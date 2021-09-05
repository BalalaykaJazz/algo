"""Сортировка выбором. О(n^2)"""


def selectionSort(nums: list[int]) -> list[int]:
    """Самый маленький элемент второй части массива помещается в конец первой части."""

    for i in range(0, len(nums)):
        minimum = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minimum]:
                minimum = j
        nums[minimum], nums[i] = nums[i], nums[minimum]

    return nums


values = [2, 8, 6, 1, 4, 3]
result = selectionSort(values)
assert result == [1, 2, 3, 4, 6, 8]
