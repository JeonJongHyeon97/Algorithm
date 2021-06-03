import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
# 노드사이의 연결을 딕셔너리로 만들기
graph ={}
for _ in range(n):
    node = list(input().split())
    graph[node[0]]=[]
    for i in node[1:]:
        graph[node[0]].append(i)

# 전위 순회 ( Preorder)
def preorder(start):
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
def inorder(start):
    global graph
    child = graph[start]

    if child[0] != '.': # left 존재
        inorder(child[0])

    print(start, end='')

    if child[1] != '.': # right 존재
        inorder(child[1])

inorder('A')
print()
# 후위 순회 (Postorder)
def postorder(start):
    global graph
    child = graph[start]

    if child[0] != '.':  # left 존재
        postorder(child[0])

    if child[1] != '.':  # right 존재
        postorder(child[1])

    print(start, end="")

postorder('A')