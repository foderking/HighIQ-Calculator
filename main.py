#!/usr/bin/python3

import bc, os
from library import *
from varname import nameof

arith = {'A': A,'M': M,'D': D,'d': d,'m': m} # arguments for the arithmetic function

def arithmetic(arg, first, second):
    """This function performs basic arithmetic on two numbers.
    it expects two numbers and an argument parameter to determine which arithmetic operation to perfom.
    return the resulting integer.
    # arguments have already been mapped to the set variables
    Arguments:
    A = additon
    D = division
    M = mulitplication
    d = integer division
    m = remainder / modulus
    """
    # arguments are stored in a dictionary, the string directly represents it.

    if arg not in arith.keys():
        raise ValueError(f'You did not give a valid argument\nValid arguments are {tuple(arith.keys())}.')
    try:
        first = float(first)
        second = float(second)
    except:
        raise ValueError('You need to give a valid number as an argument!!')

    return arith[arg](first, second)

def evaluate(expression):
    """This function takes in a string as input, and evaluates it as an expression
    returns the result 
    # expression will also be able to make use of my custom functions 
    the 'eval' function from std library is used. certain precautions are made to prevent executing certain code
    """
    # makes sure only valid inputs are given
    try:
        return eval(expression, {'__builtins__': None}, arith)
    except:
        raise ValueError('Expression contains invalid input!!.')

def ev_mod():
    """Enters evaluate mode.
    One would freely be able to evaluate expressions like in a python interpreter, but with a lot of restrictions
    """
    while True:
        print(f'You\'re in "evaluate" mode!.\nPress "q" to exit.')
        input_ = input('Type an expression: ')
        if input_ == 'q':
            break
        else:
            print(evaluate(input_))


def boolean(*args):
    """This function performs basic boolean operations on numbers.
    it expects two numbers and an argument parameter to determine which operation to perfom.
    returns the result.
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

    ev_mod()    

