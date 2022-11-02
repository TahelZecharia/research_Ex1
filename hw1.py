"""
Tahel Zecharia
"""

"""
************* Q1 *************
"""


def safe_call(func, **kwargs):
    """
    :param func:
    :param kwargs:
    :return:

    >>> safe_call(f1, x=3, y=7.0, z=2)
    12.0

    >>> safe_call(f1, x=3.2, y=7.0, z=2)
    Traceback (most recent call last):
      ...
    Exception: Invalid Input

    >>> safe_call(f2, x=2, y="abc", z=8.9)
    '2abc8.9'

    >>> safe_call(f1, x=4, y=2, z=2)
    Traceback (most recent call last):
      ...
    Exception: Invalid Input
    """

    func_annotation = func.__annotations__

    for x in func_annotation.keys():

        if (type(kwargs[x])) is not func_annotation[x]:
            raise Exception("Invalid Input")

    return func(**kwargs)

def f1(x: int, y: float, z):
    return x + y + z

def f2(x: int, y: str, z):
    return str(x) + y + str(z)

"""
************* Q2 *************
"""

def breadth_first_search(start, end, neighbor_function):
    """

    :param start:
    :param end:
    :param neighbor_function:
    :return:
     >>> breadth_first_search(start=(0,0), end=(2,2), neighbor_function= four_neighbor_function)
     (0, 0)
     (1, 0)
     (2, 0)
     (2, 1)
     (2, 2)

    """
    start_x = start[0]
    start_y = start[1]

    end_x = end[0]
    end_y = end[1]

    temp_x = start_x
    temp_y = start_y

    print((temp_x,temp_y))

    if(start_x < end_x):
        while(temp_x < end_x):
            temp_x = max(map(lambda x:x[0], neighbor_function((temp_x, temp_y))))
            print((temp_x,temp_y))

    elif (start_x > end_x):
        while (temp_x > end_x):
            temp_x = min(map(lambda x: x[0], neighbor_function((temp_x, temp_y))))
            print((temp_x,temp_y))

    if (start_y < end_y):
        while (temp_y < end_y):
            temp_y = max(map(lambda x: x[1], neighbor_function((temp_x, temp_y))))
            print((temp_x,temp_y))

    elif (start_y > end_y):
        while (temp_y > end_y):
            temp_y = min(map(lambda x: x[1], neighbor_function((temp_x, temp_y))))
            print((temp_x,temp_y))

def four_neighbor_function(node)->list:

    (x, y) = node
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
"""
************* Q3 *************
"""


def print_sorted(x):

    """

    :param x:
    :return:

    >>> print_sorted({"a": 5, "c": 6, "b": [1, 3, 2, 4]})
    {'a': 5, 'b': [1, 2, 3, 4], 'c': 6}
    >>> print_sorted((1, 3, 2, 4))
    (1, 2, 3, 4)
    >>> print_sorted([1, 3, 2, 4])
    [1, 2, 3, 4]
    """
    print(rec_sorted(x))

def rec_sorted(x):

    if type(x) is dict:

        for value in x.values():
            rec_sorted(value)
        x = dict(sorted(x.items()))

    if type(x) is tuple:

        for i in x:
            rec_sorted(i)
        x = tuple(sorted(x))

    if type(x) is set:

        x = set(sorted(x))

    if type(x) is list:

        for i in x:
            rec_sorted(i)
        x.sort()

    return x

"""
************* Q4 *************
https://www.codingame.com/ide/puzzle/power-of-thor-episode-1

my solution:

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
curr_x = initial_tx
curr_y = initial_ty

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    if(curr_x < light_x):
        if(curr_y < light_y):
            curr_x+=1
            curr_y+=1
            print("SE")
        elif(curr_y > light_y):
            curr_x+=1
            curr_y-=1
            print("NE")
        else:
           curr_x+=1 
           print("E")

    elif(curr_x > light_x):
        if(curr_y > light_y):
            curr_x-=1
            curr_y-=1
            print("NW")
        elif(curr_y < light_y):
            curr_x-=1
            curr_y+=1
            print("SW")
        else:
           curr_x-=1 
           print("W")
    
    elif(curr_y < light_y):
        curr_y+=1
        print("S")

    elif(curr_y > light_y):
        curr_y-=1
        print("N")
        
        
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # A single line providing the move to be made: N NE E SE S SW W or NW
    
"""
if __name__ == '__main__':

    import doctest
    doctest.testmod()



