from typing import Any


def binary_search(list: list[Any], item: Any) -> int | None:
    """
    Binary search algorithm to find the index of an item in a sorted list.
    :param list: A sorted list of items.
    :param item: The item to search for in the list.
    :return: The index of the item if found, otherwise None.
    """
    low = 0
    high = len(list)

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [i for i in range(100)]

print(binary_search(my_list, 3))  # 1
print(binary_search(my_list, -1))  # None
print(binary_search(my_list, 9))  # 4
print(binary_search(my_list, 99))  # 0


def max_number_of_steps():
    """
        Sorted list of 128 names.
        Maximum number of steps it would take
    """
    steps = 0
    mid = 256

    while mid > 1:
        steps += 1
        mid = mid // 2

    return steps


print("Max steps", max_number_of_steps())
