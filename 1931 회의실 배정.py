# 정렬
import sys
input = sys.stdin.readline
n = int(input())
time = [[0,0] for _ in range(n)]


for i in range(n):
    start, end = map(int, input().split())
    time[i][0] = start
    time[i][1] = end

time.sort(key = lambda x: (x[1], x[0])) # sort by end time, then start time (ascending)
last_end = time[0][1]   # first council's end time
cnt = 1

for start, end in time[1:]: # [1:] because start with count = 1
    if start >= last_end:
       cnt+=1
       last_end = end


print(cnt)

