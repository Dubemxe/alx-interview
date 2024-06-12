#!/usr/bin/python3
'''
Defines the minOperations function
'''


def minOperations(n):
    '''
    Gets fewest number of operations needed to result in exactly n H characters
    '''
    if (n < 2):
        return 0
    opera, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            opera += root
            # set n to the remainder
            n = n / root
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return opera
