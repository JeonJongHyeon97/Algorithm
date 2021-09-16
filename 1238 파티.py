import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m, x = map(int, input().split())
goPath = [[] for i in range(n + 1)]
backPath = [[] for i in range(n + 1)]
goTime = [999999] * (n + 1)
backTime = [999999] * (n + 1)

def dijkstra(start, Time, s):
    heap = []
    Time[start] = 0
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        if Time[n] >= w:
            for next_n, next_w in s[n]:
                total_W = next_w + w
                if total_W < Time[next_n]:
                    Time[next_n] = total_W
                    heappush(heap, [total_W, next_n])

for _ in range(m):
    a, b, w = map(int, input().split())
    goPath[a].append([b, w])
    backPath[b].append([a, w])

dijkstra(x, goTime, goPath)
dijkstra(x, backTime, backPath)

answer = [goTime[i] + backTime[i] for i in range(1, len(goTime))]
print(max(answer))