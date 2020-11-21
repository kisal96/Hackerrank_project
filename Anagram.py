#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the anagram function below.
def anagram(s):
    n = len(s)
    a = ''
    b = ''
    count = 0

    if len(s) % 2 == 0:

        for i in range(0, n // 2):
            a += s[i]
        for i in range(n // 2, n):
            b += s[i]

        arr = [i for i in a]

        for i in range(n // 2):
            if b[i] in arr:
                arr.remove(b[i])
            else:
                count += 1
        print(count)

    else:
        print(-1)


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)



