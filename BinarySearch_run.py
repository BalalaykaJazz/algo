from algorithms.BinarySearch import binary_search, lower_bound, upper_bound
from bisect import bisect, bisect_left, bisect_right
from typing import List


def check(store: List[int], x: int) -> int:

    # result = binary_search(store, x)
    # result_lib = bisect(store, x)
    # print(result, result_lib)
    # assert result == result_lib

    result = lower_bound(store, x)
    result_lib = bisect_left(store, x)
    print(result, result_lib)
    assert result == result_lib

    result = upper_bound(store, x)
    result_lib = bisect_right(store, x)
    print(result, result_lib)
    assert result == result_lib


# test case 1
seq = [1, 3, 4, 6, 8]
check(seq, 3)

# test case 2
seq = [1, 3, 3, 3, 5]
check(seq, 3)
