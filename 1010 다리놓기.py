# -*- coding: utf-8 -*-

import math

case_Num = int(input())

for i in range(case_Num):
    n,m = map(int, input().split())
    # result = int(math.factorial(m)/math.factorial(n)/math.factorial(m-n))
    result = int(math.factorial(m)//math.factorial(n)//math.factorial(m-n))
    
    print(result)