#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def power(a,b):
    a = a %( 10**9 + 7) 
    a2= a*a%( 10**9 + 7)
    if(b==0):
        return 1
    elif( b%2 ==0):
        m= power(a,b//2)%( 10**9 + 7)
        return m*m%( 10**9 + 7)
    else : 
        m=power(a,(b-1)//2)%( 10**9 + 7)
        return a*m*m%( 10**9 + 7)
def solve(a, b):
    print(power(a,b))
    return
    # Write your code here
    

if __name__ == '__main__':
    a = 34543987529435983745230948023948
    b = 3498573497543987543985743989120393097595572309482304
    #print(pow(a, b, 1000000007))
    solve(a,b)

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):
    #     first_multiple_input = input().rstrip().split()

    #     a = first_multiple_input[0]

    #     b = first_multiple_input[1]

    #     result = solve(a, b)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
