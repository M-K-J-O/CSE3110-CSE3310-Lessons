#j_quick_sort.py

"""
title: quick sort example
author: Marco Ou
date feb 21 2024
"""

def quickSort(LIST: list[int], FIRST_INDEX: int, LAST_INDEX: int) -> None:
    """
    Assign the first value as the pivot and place it in its correct location
    :param LIST: list (int) -> unsorted
    :param FIRST_INDEX: int
    :param LAST_INDEX: int
    :return: None
    """

    if FIRST_INDEX < LAST_INDEX:
        # tests that the list is more than one length -> base case

        pivot_value = LIST[FIRST_INDEX]
        left_index = FIRST_INDEX + 1
        right_index = LAST_INDEX

        done = False
        while not done:
            #iterative component
            while left_index <= right_index and LIST[left_index] <= pivot_value:
                left_index += 1

            while right_index >= left_index and LIST[right_index] >= pivot_value:
                right_index -= 1

            if right_index < left_index:
                # has the right pointer crossed over the left pointer?
                done = True
            else:
                temp = LIST[left_index]
                LIST[left_index] = LIST[right_index]
                LIST[right_index] = temp

        temp = LIST[FIRST_INDEX]
        LIST[FIRST_INDEX] = LIST[right_index]
        LIST[right_index] = temp

        #recursive section
        quickSort(LIST, FIRST_INDEX, right_index - 1)
        quickSort(LIST, right_index + 1, LAST_INDEX)

if __name__ == "__main__":
    from my_functions import *

    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        quickSort(NUMBERS, 0, len(NUMBERS) - 1)
        END_TIME = getTime()
        TIMES.append(END_TIME-START_TIME)
        print(i)
    print(getAverage(TIMES))

