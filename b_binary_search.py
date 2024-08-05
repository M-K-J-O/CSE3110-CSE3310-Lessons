# b_binary_search.py
"""
title: binary search example
author: Marco Ou
date-created: 2024-02-06
"""
from random import randrange


def createArray(SIZE: int = 20000000) -> list:
    """
    create and ordered array of approximate size SIZE
    :param SIZE: int
    :return: list[int]
    """
    numbers = []

    for i in range(2 * SIZE):
        if randrange(2) == 1:
            numbers.append(i)

    return numbers


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


if __name__ == "__main__":
    from time import perf_counter
    from statistics import fmean

    TRIALS = []
    NUMBERS = createArray(10000000)

    for i in range(99999):
        NUM = NUMBERS[randrange(len(NUMBERS))]
        print(NUM)
        START_TIME = perf_counter()
        FOUND = binarySearch(NUMBERS, NUM)
        END_TIME = perf_counter()
        print(FOUND)
        TRIALS.append((END_TIME - START_TIME))
    print(f"Average total time: {fmean(TRIALS)}")

    NUMBERS = createArray(20000000)
    NUM = NUMBERS[randrange(len(NUMBERS))]
    print(NUM)
    FOUND = binarySearch(NUMBERS, NUM)
    print(FOUND)
