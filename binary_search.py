def binary_search(list, item):
    """
    Binary Search guessing a item in a list using array
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

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3)) # 1
print(binary_search(my_list, -1)) # None
print(binary_search(my_list, 9)) # None


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

