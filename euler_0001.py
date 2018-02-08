#!/bin/python3

import sys

t = int(input().strip())

partial_calc = lambda n, k: (k * (n // k) * (n // k + 1) // 2)
calc = lambda n: (partial_calc(n, 3) + 
                  partial_calc(n, 5) - 
                  partial_calc(n, 15))

l = [3, 5]
for a0 in range(t):
  n = int(input().strip())
  print(calc(n - 1))
  
