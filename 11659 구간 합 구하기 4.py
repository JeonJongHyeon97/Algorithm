# -*- coding: utf-8 -*-
"""
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
"""
import sys
input = sys.stdin.readline
n , m =map(int, input().split())
num = list(map(int, input().split()))
total = [0]*(n+1)
tmp=0

for i in range(1,len(num)+1):
    total[i]=(tmp+num[i-1])
    tmp+=num[i-1]
    
for _ in range(m):
    start, end = map(int, input().split())
    print(total[end]-total[start-1])

