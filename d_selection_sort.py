# d_selection_sort.py
"""
title:Selection sort example
author: Marco Ou
date: Feb 9th 2024
"""

from my_functions import *


def selectionSort(LIST: int) -> None:
    """
    Select the lowest value in the unsorted part of the list and place it at the lowest index of the unsorted part of the list. (The values exchange places.)
    :param LIST: LIST[int]
    :return: None
    """
    for i in range(len(LIST) - 1):
        minimum_index = i
        for j in range(i + 1, len(LIST)):
            if LIST[j] < LIST[minimum_index]:
                minimum_index = j
        if LIST[minimum_index] != LIST[i]:
            TEMP = LIST[i]
            LIST[i] = LIST[minimum_index]
            LIST[minimum_index] = TEMP

if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        selectionSort(NUMBERS)
        END_TIME = getTime()
        TIMES.append(END_TIME-START_TIME)
        print(i)
    print(getAverage(TIMES))