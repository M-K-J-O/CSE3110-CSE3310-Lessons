# j_heap_sort.py

"""
Title: Heap sort
Author: Marco Ou
Date: feb 23rd 2024
"""


def heapify(LIST: list[int], LEN_ARRAY: int, ROOT_INDEX: int) -> None:
    """
    heapifies all subtress in the binary tree
    :param LIST:  list[int]
    :param LEN_ARRAY: int
    :param ROOT_INDEX: int -> parent index
    :return: None
    """

    largest_index = ROOT_INDEX
    left_index = 2 * ROOT_INDEX + 1
    right_index = 2 * ROOT_INDEX + 2

    # test if the left child value is larger than the largest index value
    if left_index < LEN_ARRAY and LIST[ROOT_INDEX] < LIST[left_index]:
        largest_index = left_index

    # test if the right child value is larger than the largest index value
    if right_index < LEN_ARRAY and LIST[largest_index] < LIST[right_index]:
        largest_index = right_index

    # test if the largest index value is no longer the root index
    if largest_index != ROOT_INDEX:
        temp = LIST[ROOT_INDEX]
        LIST[ROOT_INDEX] = LIST[largest_index]
        LIST[largest_index] = temp

        # heapify the ROOT -> Recursive section
        heapify(LIST, LEN_ARRAY, largest_index)


def heapsort(LIST: list[int]) -> None:
    """
    uses heap sort algoirthms to sort the array
    :param LIST:  list[int] -> unsorted
    :return: None
    """

    length_array = len(LIST)

    # build the max heap
    for i in range(length_array, -1, -1):
        heapify(LIST, length_array, i)

    # one by one, extract an element and heapify
    for i in range(length_array - 1, 0, -1):
        temp = LIST[i]
        LIST[i] = LIST[0]
        LIST[0] = temp
        heapify(LIST, i, 0)


if __name__ == "__main__":
    from my_functions import *

    for i in range(30):
        TIMES = []
        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        heapsort(NUMBERS)
        END_TIME = getTime()
        print(i)

        TIMES.append(END_TIME - START_TIME)

    print(getAverage(TIMES))
