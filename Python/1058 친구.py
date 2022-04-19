# -*- coding: utf-8 -*-
"""
지민이는 세계에서 가장 유명한 사람이 누구인지 궁금해졌다. 가장 유명한 사람을 구하는 방법은 각 사람의 2-친구를 구하면 된다. 어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, A와 친구이고, B와 친구인 C가 존재해야 된다. 여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다. 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.

A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.
"""
# 주어진 친구 관계 행렬을 토대로, 2-친구 관게 행렬을 만든다.
# Floyd-Warshall 알고리즘

n = int(input())
ynList = [list(input()) for _ in range(n)]

count=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if j==k:    #자기 자신은 제외
                continue
            if ynList[j][k] == 'Y' or (ynList[j][i] =='Y' and ynList[i][k] == 'Y'):
                count[j][k] = 1
    
    
maxFriend=0
for i in count:
    maxFriend=max(maxFriend, sum(i))
    
    
print(maxFriend)