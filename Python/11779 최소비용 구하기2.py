import heapq
import sys

input = sys.stdin.readline

def dijkstra(s):
    distance = [INF] * (n + 1)
    distance_path = [[] for _ in range(n + 1)]
    queue = [[0, s, [s]]]
    distance[s] = 0

    while queue:

        now_cost, now_node, path = heapq.heappop(queue)

        for next_cost, next_node in graph[now_node]:
            if next_cost + now_cost < distance[next_node]:
                total_cost = next_cost + now_cost
                distance[next_node] = total_cost
                path.append(next_node)
                distance_path[next_node] = path
                heapq.heappush(queue, [total_cost, next_node, path])

    return distance, distance_path


INF = 99999

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())

    graph[start].append([cost, end])

start_city, end_city = map(int, input().split())
answer, answer_path = dijkstra(start_city)

print(answer[end_city])
print(len(answer_path[end_city]))

for element in answer_path[end_city]:
    print(element, end = " ")