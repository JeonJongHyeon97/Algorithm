from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
dict = defaultdict(list) # 친구관계
for _ in range(int(input())):
    a, b = map(int, input().split())
    dict[a].append(b)
    dict[b].append(a)

invited = []
visited = [1]
for friend in dict[1]:
    if friend not in visited:
        visited.append(friend)
        invited.append(friend)
for friend in invited.copy():
    for next_friend in dict[friend]:
        if next_friend not in visited:
            visited.append(next_friend)
            invited.append(next_friend)
print(len(invited))

