import math
import os
import random
import re
import sys

def solve(s):
    
    k = s.split(" ")
    kk = []
    for i in k:
        kk.append(i.capitalize())
    
    
    return " ".join(kk)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
