# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline
from collections import defaultdict
n, m = map(int, input().split())
graph = defaultdict(list)

def DFS(start):
    for j in graph[start]:
        if j not in visited:
            visited.append(j)
            DFS(j)
cnt = 0

for _ in range(m):
    key, value = map(int, input().split())
    graph[key].append(value)
    graph[value].append(key)

visited = []
for i in graph.keys():
    print("key : "i)
    print("visited : ", visited)
    if i not in visited:
        print("첫 탐색 -- ",i)
        visited.append(i)
        cnt+=1
        start = i
        while len(visited) != 6:
            for j in graph[start]:
                if j not in visited:
                    visited.append(j)
                    start = j
                
print(cnt)
    
    
