import math

PI = 3.14


def add(a, b):
    return a + b


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


print(add(5, 7))

factorial(5)