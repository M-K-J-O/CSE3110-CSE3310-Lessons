# f_factorials.py
"""
title: factorial recursion
author: Marco Ou
date-created: 2024-02-13
"""


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


if __name__ == "__main__":
    NUM = int(input("Enter a number: "))

    FACTORIAL = recursiveFactorial(NUM)

    print(f"The factorial of {NUM} is {FACTORIAL}.")
