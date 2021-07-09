import sys
from collections import defaultdict

input = sys.stdin.readline
relation = defaultdict(list)

n = int(input())
start, end = map(int, input().split())
for _ in range(int(input())):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)
answer=-1
def DFS(queue):
    global answer
    if queue[-1] == end:
        answer = len(queue)-1
        return
    for i in relation[queue[-1]]:
        if i not in queue:
            queue.append(i)
            DFS(queue)
            queue.pop()
DFS([start])
print(answer)