# -*- coding: utf-8 -*-
"""
지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. 
(이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.
"""
# collection 의 deque.rotate를 사용

from collections import deque
n, m = map(int, input().split())
que = deque(range(1, n+1))
count=0
num=list(map(int, input().split()))
for i in range(len(num)):
    # print("\ntarget : ", num[i])
    # print(que.index(num[i]))
    # print(len(que)-que.index(num[i]))
    if num[i] == que[0]:
        que.popleft()
    elif que.index(num[i]) > len(que)-que.index(num[i]):
        count+=abs(len(que)-que.index(num[i]))
        # print("move : ",len(que)-que.index(num[i]))
        que.rotate(len(que)-que.index(num[i]))
        
        # print(que.popleft())
        # print("2",que)
    elif que.index(num[i]) <= len(que)-que.index(num[i]):
        count+=abs(que.index(num[i]))
        # print("move : ",-(que.index(num[i])))
        que.rotate(-(que.index(num[i])))
        
        # print(que.popleft())
        # print("3",que)

print(count)       
        
        
        
        
        
        
        
que = deque([3, 4, 5, 6, 7, 8, 9, 10, 1])
print(que)
que.rotate(3)
print(que)



