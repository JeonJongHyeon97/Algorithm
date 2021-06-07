# DFS, BFS 정석
# 재귀와, queue이용

import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = {}
for i in range(n):
    graph[i+1]=[]
for _ in range(m):
    key, value = map(int, input().split())
    if value not in graph[key]:
        graph[key].append(value)
        graph[key]=sorted(graph[key])
    if key not in graph[value]:
        graph[value].append(key)
        graph[value] = sorted(graph[value])

#DFS
visited = []
def DFS(start):
    global visited
    visited.append(start)
    if graph[start]:
        for i in graph[start]:
            if i not in visited:    # 이미 방문한 노드인지 확인
                DFS(i)  # 재귀를 이용해 깊이 우선 탐색

DFS(v)
print(*visited)


#BFS
queue = deque([v])
visited = []
def BFS(start):
    global queue
    while queue:
        start = queue.popleft() # 선입선출
        if start not in visited:    # 이미 방문한 노드인지 확인
            visited.append(start)
            for i in graph[start]:
                queue.append(i)

BFS(v)
print(*visited)

