# -*- coding: utf-8 -*-
# 최소공약수 이용하기

import sys
import math     # using math library to use gcd
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
first = num[0]
for i in range(1,len(num)):
    a = num[i]//math.gcd(first,num[i])
    b = first//math.gcd(first, num[i])
    print(f"{b}/{a}")   # f-string can use 3.6 or later