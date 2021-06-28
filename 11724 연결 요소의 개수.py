# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline
from collections import defaultdict, deque
n, m = map(int, input().split())
graph = defaultdict(list)
queue = deque()

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

visited = [False]+[True for _ in range(n)]
for i in range(1,n+1):
    if visited[i]:
        visited[i]=False
        cnt+=1
        queue.append(i)
        while queue:
            node = queue.pop()
            for j in graph[node]:
                if visited[j]:
                    visited[j]=False
                    queue.append(j)
                
print(cnt)
    
    
