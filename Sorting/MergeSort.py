"""Сортировка слиянием. O(n log n)"""


def merge(left_list: list[int], right_list: list[int]):
    """Список разделяется пополам и обрабатывается рекурсивно."""

    sorted_list = []
    left_index, right_index = 0, 0
    left_size, right_size = len(left_list), len(right_list)

    for _ in range(left_size + right_size):
        if left_index < left_size and right_index < right_size:
            if left_list[left_index] <= right_list[right_index]:
                sorted_list.append(left_list[left_index])
                left_index += 1
            else:
                sorted_list.append(right_list[right_index])
                right_index += 1

        elif left_index == left_size:
            sorted_list.append(right_list[right_index])
            right_index += 1
        elif right_index == right_size:
            sorted_list.append(left_list[left_index])
            left_index += 1

    return sorted_list


def mergeSort(numbers: list[int]):

    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2

    left_list = mergeSort(numbers[:middle])
    right_list = mergeSort(numbers[middle:])

    return merge(left_list, right_list)


def TestSmallSizes():
    numbers = []
    sorted_list = mergeSort(numbers)
    assert sorted_list == []

    numbers = [1]
    sorted_list = mergeSort(numbers)
    assert sorted_list == [1]

    numbers = [1, 2]
    sorted_list = mergeSort(numbers)
    assert sorted_list == [1, 2]

    numbers = [2, 1]
    sorted_list = mergeSort(numbers)
    assert sorted_list == [1, 2]

    print("TestSmallSizes OK")


def TestSorted():
    numbers = [1, 2, 3, 4, 5, 10, 20, 40]
    sorted_list = mergeSort(numbers)
    assert sorted_list == numbers

    numbers = [40, 20, 5, 3, 2, 1]
    sorted_list = mergeSort(numbers)
    assert sorted_list == [1, 2, 3, 5, 20, 40]

    print("TestSorted OK")


if __name__ == "__main__":
    array = [120, 45, 68, 250, 176]
    array = mergeSort(array)
    assert array == [45, 68, 120, 176, 250]

    TestSmallSizes()
    TestSorted()
