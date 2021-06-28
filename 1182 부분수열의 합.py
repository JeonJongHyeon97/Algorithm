# -*- coding: utf-8 -*-
# DFS 백트랙킹

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
num = list(map(int, input().split()))
num = sorted(num)
cnt = 0

def dfs(queue, visited):

    global cnt
    if sum(queue) == s:
        cnt+=1
        print(queue)
        print(visited)
        print()
    if sum(queue) > s or len(queue) == n:
        return
    for i in range(len(num)):
        no = num[i]
        if i < visited[-1]:
            continue
        if i not in visited:
            queue.append(no)
            visited.append(i)
            dfs(queue, visited)
            queue.pop()
            visited.pop()
            

for i in range(len(num)):
    queue = [num[i]]
    dfs(queue, [i])
print(cnt)