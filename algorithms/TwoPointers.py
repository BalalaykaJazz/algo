
def solve_find_segment(store: list[int], x: int) -> tuple[int, int]:
    right_position = 0
    sum = 0

    for left_position in range(len(store)):

        while right_position < len(store) and sum < x:
            sum += store[right_position]
            right_position += 1

        if sum == x:
            return left_position + 1, right_position

        sum -= store[left_position]

    return 1, 0


values = [3, 1, 5, 6, 2, 8, 7]
target = 18

result = solve_find_segment(values, target)
# print(result)


def solve_sorted_seq(store_first: list[int], store_second: list[int], x: int) -> tuple[int, int]:
    right_position = len(store_second) - 1

    for left_position in range(len(store_first)):

        while right_position >= 0 and (store_first[left_position] + store_second[right_position]) > x:
            right_position -= 1

        if right_position >= 0 and (store_first[left_position] + store_second[right_position]) == x:
            return left_position + 1, right_position + 1

    return -1, -1


values1 = [0, 2, 5]
values2 = [-3, -1, 2]
target = 24

result = solve_sorted_seq(values1, values2, target)
print(result)

