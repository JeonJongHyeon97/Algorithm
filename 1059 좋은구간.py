# -*- coding: utf-8 -*-
"""
정수 집합 S가 주어졌을때, 다음 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 한다.
A와 B는 양의 정수이고, A < B를 만족한다.
A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수를 구해보자.
"""

num = int(input())
num_list = list(map(int, input().split()))
n = int(input())
num_list = sorted(num_list)
# print(num_list)
answer = []
if (n in num_list):
    print(0)
else:
    for i in range(len(num_list)-1):
        start = num_list[i]+1
        end = num_list[i+1]-1
        # print(start)
        # print(end)
        if(start<=n and n<=end):
            print((n-start)*(end-n)+(end-start))
