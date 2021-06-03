# BFS
# 미리 100001개의 배열을 만들고, 해당 칸에 왔을때 걸리는 초를 넣어줌


from collections import deque

n, k = map(int, input().split())
q = deque([n])
visited = [None for _ in range(100001)]
visited[n] = 0

while q:
    node = q.popleft()
    if node == k:
        print(visited[node])
        break
    else:
        next_node = [node - 1, node + 1, node * 2]  # 갈 수 있는 경우의 수
        for next_ in next_node:
            if 0 <= next_ <= 100000 and visited[next_] is None: # 범위안이고, 해당칸에 처음 온거라면,
                visited[next_] = visited[node] + 1  # 1초 증가
                q.append(next_) # 큐에 추가