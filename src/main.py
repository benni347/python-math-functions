#!/usr/bin/python3
"""
This is the main file to run.
Author: benni347@github.com
"""
FUNCTIONS_TOTAL = 1


def sigma(expression, low=0, high=None):
    """
    This is for the sigma notation.
    :param expression: str
    :param low: int
    :param high: int
    :return:
    :TODO: Add the TUI Sigma Symbol.  
    """
    var = low
    expr = expression
    x = low
    sum_sigma = low

    while x <= high:
        for i in high:
            sum_sigma += i
        x += 1
    print(sum_sigma)
    return sum_sigma


running = True
while running:
    print("Which math function do you want to use?")
    print("1) Sigma (Sum, from, to)")
    input_f = input()
    try:
        int(input_f)
    except ValueError:
        print("Please put in a digit.")
    # if input_f is not input_f.isnumeric():
    #     print("Please put in a digit")
    # print(input_f.isnumeric())
    if input_f > str(FUNCTIONS_TOTAL):
        print("You entered a number that is not in the list.")
    if input_f == "1":
        print("Please put in the expression, start number, high number:")
        expr = input("expression: ")
        start = int(input("start: "))
        end = int(input("high: "))
        sigma(expr, start, end)
