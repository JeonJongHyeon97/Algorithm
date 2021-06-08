import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
# make graph
graph ={}
for _ in range(n):
    node = list(input().split())
    graph[node[0]]=[]
    for i in node[1:]:
        graph[node[0]].append(i)

# 전위 순회 ( Preorder)
def preorder(start: str):
    print(start, end='')
    global graph
    child = graph[start]

    if child == ['.','.']:
        return

    for i in child:
        if i != '.':
            preorder(i)

preorder('A')
print()
# 중위 순회 (Inorder)
def inorder(start: str):
    global graph
    child = graph[start]

    if child[0] != '.': # left child
        inorder(child[0])

    print(start, end='')

    if child[1] != '.': # right child
        inorder(child[1])

inorder('A')
print()
# 후위 순회 (Postorder)
def postorder(start: str):
    global graph
    child = graph[start]

    if child[0] != '.':  # left child
        postorder(child[0])

    if child[1] != '.':  # right child
        postorder(child[1])

    print(start, end="")

postorder('A')