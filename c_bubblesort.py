# c_bubblesort.py
"""
title: bubble sort example
author: Marco Ou
date: feb 8th 2024
"""

from my_functions import *


def bubbleSort(LIST: int) -> None:
    """
    compares two adjacent values and moves the highest one to the end of the list.
    :param LIST:  List[int]
    :return: None (lists persist inside and outside of a function)
    """
    for i in range(len(LIST) - 1, 0, -1):  # traversing backwards from the end of the list to index 1
        for j in range(i):
            # traversing forward in the unsorted section of the list
            if LIST[j] > LIST[i]:  # if the left number is larger than the right number
                TEMP = LIST[j]
                LIST[j] = LIST[j + 1]
                LIST[j + 1] = TEMP

if __name__ == "__main__":

    TIMES = []

    for i in range(5):
        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        bubbleSort(NUMBERS)
        END_TIME = getTime()
        TIMES.append(END_TIME-START_TIME)
        print(i)
    print(getAverage(TIMES))

