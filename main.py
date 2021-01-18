#!/usr/bin/python3

import bc
from library import *
from varname import nameof

arith = {'A': A,'M': M,'D': D,'d': d,'m': m} # arguments for the arithmetic function

def arithmetic(arg, first, second):
    """This function performs basic arithmetic on two numbers.
    it expects two numbers and an argument parameter to determine which arithmetic operation to perfom.
    return the resulting integer.
    # arguments should have already been mapped to the set variables
    Arguments:
    A = additon
    D = division
    M = mulitplication
    d = integer division
    m = remainder / modulus
    """
    # arguments are stored in a dictionary, the string directly represents it.
    return arith[arg](first, second)

def boolean(*args):
    """This function performs basic boolean operations on numbers.
    it expects two numbers and an argument parameter to determine which operation to perfom.
    returns the result.
    """

def evaluate(string):
    """This function takes in a string as input, and evaluates it as an expression
    returns the result 
    """

def var(name, value):
    """This function stores the value in the variable 'name'
    the result is kept in a dictionary
    """

def func():
    """Library of popularly used functions
    rough idea i have is to reserve names for different functions, and the user could use those names arguments to perform those functions on the number. 
    ex: math.sqrt would be mapped to 'sqr', so if user types 'sqr 56', the program would know to return the root of 56
    """


from random import randint
from time import sleep

def test_ar():
    while True:
        for arg in arith.keys():
            sleep(1)
            f = randint(-999,999)
            s = randint(-999,999)
            print(f'operation: {arg} on {f} and {s}\n{ arithmetic(arg, f , s) }\n')

if __name__ == '__main__' :
    """the program starts with an iteractive environment. essentially a while loop to wait for the next instruction
    other environments can be specified.
    """
    test_ar()

