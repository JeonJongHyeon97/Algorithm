import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
graph=defaultdict(list)
queue = deque([1])
matrix = [[0 for _ in range(V)] for i in range(V)]
shortest_path=[10 for _ in range(V)]
print(matrix)
for _ in range(E):
    u, v, w = map(int, input().split())
    if matrix[u-1][v-1] == 0:
        matrix[u-1][v-1] = w
    else:
        matrix[u-1][v-1] = min(matrix[u-1][v-1], w)

while queue:













