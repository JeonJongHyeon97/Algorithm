import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())
mat = defaultdict(list)
parent = [0 for _ in range(n+1)]
parent[1] = 1
for _ in range(n-1):
    a, b = map(int, input().split())
    mat[a].append(b)
    mat[b].append(a)
queue = deque([1])
while queue:
    print(queue)
    root = queue.popleft()
    for j in mat[root]:
        if parent[j] == 0:
            parent[j] = root
            queue.append(j)


for i in parent[2:]:
    print(i)

