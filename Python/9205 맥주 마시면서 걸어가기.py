from collections import deque
import sys

input = sys.stdin.readline


def manhattan(a, b):
    return (abs(a[0] - b[0]) + abs(a[1] - b[1])) <= 1000


for _ in range(int(input())):
    n = int(input())
    nodes = []
    visited = []
    happy = False
    for j in range(n + 2):
        nodes.append(list(map(int, input().split())))
    queue = deque([nodes.pop(0)])
    destination = nodes[-1]
    nodes.sort(key=lambda x: x[0] + x[1], reverse=True)
    while queue:
        start = queue.pop()
        visited.append(start)
        if start == destination:
            happy = True
            break
        for node in nodes:
            if node not in visited and manhattan(start, node):
                queue.append(node)
    if happy:
        print("happy")
    else:
        print("sad")
