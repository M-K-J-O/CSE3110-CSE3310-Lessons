#i_merge_sort.py

"""
title: Merge Sort Example
author: Marco Ou
date: February 15th, 2024
"""



def mergeSortedLists(LIST_LEFT: list[int],LIST_RIGHT: list[int]) -> list[int]:
    """
    Iterative merge of two sorted lists
    :param LIST_LEFT: list[int] -> sorted
    :param LIST_RIGHT: list[int] -> sorted
    :return: list[int] -> sorted
    """
    #special case: one or bth lists are empty
    if len(LIST_LEFT) == 0:
        return LIST_RIGHT
    elif len(LIST_RIGHT) == 0:
        return LIST_LEFT


    # general case
    index_left = 0
    index_right = 0
    list_merge = []
    list_length_total = len(LIST_LEFT) + len(LIST_RIGHT)


    while len(list_merge) < list_length_total:
        if LIST_LEFT[index_left] <= LIST_RIGHT[index_right]:
            # checks of the left value is smaller than the right value
            list_merge.append(LIST_LEFT[index_left])
            index_left += 1
        else:
            # place the right as it's bigger
            list_merge.append(LIST_RIGHT[index_right])
            index_right += 1

        # optimization - check if one list is done

        if index_right == len(LIST_RIGHT):
            # reached the end of the right list, append the rest of the left list.
            list_merge = list_merge + LIST_LEFT[index_left:]
        elif index_left == len(LIST_LEFT):
            # reached the end of the left list, append the rest of the right list.
            list_merge = list_merge + LIST_RIGHT[index_right:]
            break
    return list_merge

def mergeSort(LIST: list[int]) -> list[int]:
    """
    performs the recursive split of the list.
    :param LIST: list[int]
    :return: list[int] -> sorted
    """

    if len(LIST) <= 1:
        return LIST # base case
    else:
        midpoint_index = len(LIST)//2
        left_list = LIST[:midpoint_index]
        right_list = LIST[midpoint_index:]
        # the following line is the recursive statement
        return mergeSortedLists(mergeSort(left_list), mergeSort(right_list))



if __name__ == "__main__":
    from my_functions import *

    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        TIMES_START = getTime()
        NEW_NUMBERS = mergeSort(NUMBERS)
        TIMES_END = getTime()
        TIMES.append(TIMES_END-TIMES_START)
        print(i)
    print(getAverage(TIMES))


