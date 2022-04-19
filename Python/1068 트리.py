from collections import defaultdict
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
parent = list(map(int, input().split()))
remove = int(input())
tree = defaultdict(list)
for node in range(len(parent)):
    tree[parent[node]].append(node)
tree[remove].clear()
queue = deque([tree[-1].pop()])
answer = 0
while queue:
    start = queue.popleft()
    if start != remove and (len(tree[start]) == 0 or tree[start] == [remove]):
        answer += 1
        continue
    for node in tree[start]:
        queue.append(node)
print(answer)
