# 다익스트라 알고리즘
# 우선순위 큐 사용 : 가중치가 작은 노드부터 탐색하는 것이 유리하므로

import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline
inf = sys.maxsize
V, E = map(int, input().split())
k = int(input())

heap=[]
graph=defaultdict(list)
shortest_path=[inf for _ in range(V+1)]


for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    
    
def dijkstra(start):
    shortest_path[start] = 0    # start node
    heappush(heap, (0, start))  # start node's cost(weight) = 0
    
    while heap:
        weight, next_node = heappop(heap)
        
        if shortest_path[next_node] >= weight:    # if existed path is not shortest   
            for w, n_n_node in graph[next_node] :
                next_weight = weight + w    # weight = existing weight + new weight
                
                if next_weight < shortest_path[n_n_node]:   # if new path is shortest (smaller weight)  
                    shortest_path[n_n_node] = next_weight
                    heappush(heap, (next_weight, n_n_node)) # start search from new node
                    
    for i in shortest_path[1:]:
        print(i if i != inf else "INF")
        
dijkstra(k)







