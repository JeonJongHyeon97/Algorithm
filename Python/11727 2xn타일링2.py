# -*- coding: utf-8 -*-
"""
2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.
"""
#Dynamic programming

n = int(input())

dp_list=[0,1,3]
for i in range(3,n+1):
    dp_list.append(dp_list[i-1]+dp_list[i-2]*2)
print(dp_list[n]%10007)
