# a_linear_search.py
"""
title: Linear Search Example
author: Marco Ou
date: 2024-02-05
"""
import random
import time
import statistics


### --- INPUTS

def recurSearch(LIST, VALUE):
    '''
    Search Linearly through the list to find our value
    :param LIST: LIST[int]
    :param VALUE: int
    :return: bool
    '''

    if len(LIST) > 0:
        if LIST[0] == VALUE:
            return True
        else:
            return recurSearch(LIST[1:], VALUE)


### --- PROCESSING
# create the list of numbers
NUMBERS = []
for i in range(200):
    VAR = random.randrange(2)
    if VAR == 1:
        NUMBERS.append(i)
for i in range(30):
    # Choose a random number
    NUM = NUMBERS[random.randrange(len(NUMBERS))]
    print(NUM)

    TRIAL = []
    # Search for our chosen value
    START_TIME = time.perf_counter()
    for i in range(len(NUMBERS)):
        if NUMBERS[i] == NUM:
            print("found!")
            break
    END_TIME = time.perf_counter()
    TRIAL.append(END_TIME - START_TIME)
### --- OUTPUTS
print(NUM)
print(f"Average total time: {statistics.fmean(TRIAL)}")
