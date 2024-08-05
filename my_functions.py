# my_functions.py
"""
title:Common functions for the unit
author: you
date: Feb 8th 2024
"""

import random
import time
import statistics


def getSmallList() -> list:
    '''
    return a small list of intergers
    :return: list[int]
    '''
    return [5, 1, 19, 3, 11, 17, 7, 13]


def getList(SIZE: int) -> list:
    """
    return a sorted list of approximate size SIZE
    :param SIZE: int
    :return: list[int]
    """
    numbers = []
    for i in range(2 * SIZE):
        if random.randrange(2) == 1:
            numbers.append(i)
    return numbers


def getRandomList(SIZE: int) -> list:
    '''
    return an unordered list of numbers of approximate size, SIZE
    :param SIZE: int
    :return: list[int]
    '''
    sorted_list = getList(SIZE)
    random.shuffle(sorted_list)
    return sorted_list


def getTime() -> float:
    """
    return the performance counter time
    :return: float
    """
    return time.perf_counter()


def getAverage(TIMES: list[float]) -> float:
    """
    returns the average time of the given list of float
    :param TIMES: list[float]
    :return: float
    """
    return statistics.fmean(TIMES)


def binarySearch(LIST, VALUE):
    """
    Search for a value within a list
    :param LIST:  list[int]
    :param VALUE: int
    :return: bool
    """

    start_index = 0
    end_index = len(LIST) - 1

    while start_index <= end_index:
        midpoint_index = (start_index + end_index) // 2
        if LIST[midpoint_index] == VALUE:
            return True
        elif VALUE > LIST[midpoint_index]:
            start_index = midpoint_index + 1
        else:
            end_index = midpoint_index - 1
    return False


def bubbleSort(LIST: list[int]) -> None:
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


def selectionSort(LIST: list[int]) -> None:
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


def insertionSort(LIST: list[int]) -> None:
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


def recursiveFactorial(NUMBER: int) -> int:
    """
    calculates the factorial of the give number
    :param NUMBER: int
    :return: int
    """
    if NUMBER == 0:
        # base case
        return 1
    else:
        # simplifies the input value
        return NUMBER * recursiveFactorial(NUMBER - 1)
