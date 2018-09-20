import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dict = {}
    result = 0
    for each in ar:
        if each not in dict:
            dict[each] = 0
        dict[each]+=1
    for every in dict.keys():
        result += int(dict[every]/2)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    
    ar = list(map(int, input().rstrip().split()))
    
    result = sockMerchant(n, ar)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()
