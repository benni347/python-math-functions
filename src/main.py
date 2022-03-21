#!/usr/bin/python3
"""
This is the main file to run.
Author: benni347@github.com
"""
FUNCTIONS_TOTAL = 3


class Main:
    """
    This is the main function,
    it is just used to get to the right math func.
    """

    def __init__(self):
        self.func = FUNCTIONS_TOTAL
        self.input_f = None

    def get_math_func(self):
        """
        Ask the user which math func he wants to use.
        """
        print("Which math function do you want to use?")
        print("1) Factorial\n"
              "2) Odd or even\n"
              "3) Factor")
        self.input_f = input()
        self.check_input()

    def check_input(self):
        """
        Validate the user input.
        """
        right_input = True
        try:
            int(self.input_f)
        except ValueError:
            print("Please put in a digit.")
            right_input = False
        if self.input_f > str(self.func):
            print("You entered a number that is not in the list.")
            right_input = False
        if right_input:
            self.call_function()

    def call_function(self):
        """
        Call the given math func.
        """
        if self.input_f == "1":
            Factorial().get_number()
        elif self.input_f == "2":  # odd or even
            print(
                "Please input the method you want to do\n"
                "1) check if even or odd\n"
                "2) calculate nth odd\n"
                "3) calculate nth even"
            )
            x = int(input())  # Define which function to use
            if x >= 4:
                print("You inputted a to high number.")
            else:
                OddEven().get_number(x)
        elif self.input_f == "3":
            Factor().get_number()
        exit(0)


# def sigma(expression, low=0, high=None):
#     """
#     This is for the sigma notation.
#     :param expression: str
#     :param low: int
#     :param high: int
#     :return:
#     :TODO: Add the TUI Sigma Symbol.
#     """
#     var = low
#     expr = expression
#     x = low
#     sum_sigma = low
#
#     while x <= high:
#         for i in high:
#             sum_sigma += i
#         x += 1
#     print(sum_sigma)
#     return sum_sigma
#
#
# def integral(lower, upper, expr, var):
#     """
#     THis will calculate the integral from lower to upper.
#     :param lower: float
#     :param upper: float
#     :param expr: str
#     :param var: str
#     :return:
#     """
#     return None


class OddEven:
    def __init__(self):
        self.func = 1
        self.n = None

    def get_number(self, func):
        """
        This will get n.
        """
        self.func = func
        self.n = input("Which number to use: ")
        self.n = int(self.n)
        self.use_right_func()

    def use_right_func(self):
        """
        1=check if odd or even
        2=calculate nth odd
        3=calculate nth even
        :return:
        """
        if self.func == 1:
            self.check_odd_or_even()
        elif self.func == 2:
            self.calculate_nth_odd()
        elif self.func == 3:
            self.calculate_nth_even()

    def check_odd_or_even(self):
        """
        Check if the number is odd or even
        :return: str: "even" or "odd"
        """
        self.n = self.n % 2
        if self.n == 1:
            print("odd")
            return "odd"
        else:
            print("even")
            return "even"

    def calculate_nth_odd(self):
        """
        Calculate the nth odd number.
        E. g:
        input: 2
        expected output: 3
        :return:
        """
        self.n = 2 * self.n - 1
        print(self.n)
        return self.n

    def calculate_nth_even(self):
        """
        Calculate the nth even number.
        E. g:
        input: 2
        expected output: 4
        :return: int
        """
        self.n = 2 * self.n
        print(self.n)
        return self.n


class Logarithm:
    def __init__(self, notation, base, n):
        self.x = None
        self.find_right_log(notation, base, n)

    def find_right_log(self, notation, base, n):
        """

        :param n:
        :param base:
        :param notation: str
        :return:
        """
        if notation == "ln":
            self.ln(n)
        elif notation == "lb":
            self.lb(n)
        else:  # If the input isn't a correct notation just use normal log
            self.log(base, n)

    def log(self, base=None, n=10.00):
        """
        This will be used for calculation logarithm
        :param notation: str
        :param base: None
        :param n: float
        :return:
        """
        self.x = None
        return None

    def ln(self, n):
        """
        Natural log, with euler's constant
        :param n: float
        :return:
        """
        return None

    def lb(self, n):
        """
        binary log
        :param n:
        :return:
        """
        return None


class Calculus:
    """
    This is the class for mainly calculus functions.
    """

    def __init__(self):
        self.x = None

    def limit(self):
        """
        This will try to calculate the limit of the fiven input
        :return:
        """
        return None


class Factorial:
    """
    This will calculate factorial
    """

    def __init__(self):
        self.n = None
        self.x = 1

    def get_number(self):
        """
        This will get n.
        """
        self.n = input("Which number to use: ")
        self.n = int(self.n)
        self.calculate_nth_factorial()

    def calculate_nth_factorial(self):
        """
        This is the method which will calculate it.
        :return:
        """
        idx = 1
        while idx <= self.n:
            self.x = self.x * idx
            idx += 1
        print(self.x)
        return self.x


class Factor:
    """
    This will factor a given number.
    """

    def __init__(self):
        self.idx = 2
        self.mod = None
        self.factor_list = []
        self.n = None

    def get_number(self):
        """
        This will get n.
        """
        self.n = input("Which number to use: ")
        self.n = int(self.n)
        self.factor()

    def factor(self):
        """
        This will factor the given number.
        :return:
        """
        self.mod = self.n % self.idx
        while self.idx <= self.n:
            if self.mod == 0:
                self.factor_list += str(self.idx)
            self.idx += 1
        print(self.factor_list)


def calc_nth_prime(location):
    """
    THis will try to calculate the nth prime
    :param location: int
    :return:
    """
    return None


running = True
while running:
    main = Main()
    main.get_math_func()
