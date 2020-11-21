#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the camelcase function below.
def camelcase(s):
    result = [i for i in s if i.isupper()]
    print(len(result) + 1)


if __name__ == '__main__':
    s = input()

    result = camelcase(s)

