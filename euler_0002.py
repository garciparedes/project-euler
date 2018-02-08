#!/bin/python3

import sys
import math

calculate = lambda k: (((2 + math.sqrt(5)) ** (k + 1)  -
                        (2 - math.sqrt(5)) ** (k + 1)) / math.sqrt(5))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    c = 0
    i = 0
    a = calculate(i)
    while n >= a:
      c += a
      i += 1
      a = calculate(i)
    print(round(c))
