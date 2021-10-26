import random
import sys


def RandomPrint(numbers: list[int]):
    """Выводит к консоль все элементы списка в случайном порядке."""

    rPointer = len(numbers) - 1

    while rPointer > 0:
        random_index = random.randrange(0, rPointer)
        print(numbers[random_index])

        numbers[random_index], numbers[rPointer] = numbers[rPointer], numbers[random_index]

        rPointer -= 1

    print(numbers[0])


if __name__ == "__main__":
    seq = sys.stdin.readline().strip().split()
    seq = [int(x) for x in seq]

    # seq = [10, 11, 12, 13, 14, 15]
    
    RandomPrint(seq)
