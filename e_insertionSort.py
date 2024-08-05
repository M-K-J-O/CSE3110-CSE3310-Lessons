# e_insertionsort.py

'''
title: Insertion SOrt
author:Marco OU
date: 2022-09-15
'''

from my_functions import *


def insertionSort(LIST: int) -> None:
    """
    takes the lowest index value in the unsorted half of the list and places it in the relative sorted half of the list.
    :param LIST: list (int)
    :return: None
    """

    for i in range(1, len(LIST)):

        INDEX_VALUE = LIST[i]

        SORTED_INDEX = i - 1

        while SORTED_INDEX >= 0 and INDEX_VALUE < LIST[SORTED_INDEX]:
            # sorted index is bigger than - and the sorted value is bigger than the index value. Then the sorted values move up one by one.
            LIST[SORTED_INDEX] = LIST[SORTED_INDEX]
            SORTED_INDEX = SORTED_INDEX - 1
        LIST[SORTED_INDEX + 1] = INDEX_VALUE  # places the index value in its relative position in the sorted list.


if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        insertionSort(NUMBERS)
        END = getTime()
        TIMES.append(END - START)
    print(getAverage(TIMES))
