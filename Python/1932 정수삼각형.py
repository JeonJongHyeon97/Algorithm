import sys
input = sys.stdin.readline
n = int(input())
triangle = []
for _ in range(n):
    tmp =[0]
    tmp.extend(list(map(int, input().split())))
    tmp.append(0)
    triangle.append(tmp)
for i in range(1,n):
    for j in range(1,i+2):
        triangle[i][j]=max(triangle[i-1][j-1]+triangle[i][j], triangle[i-1][j]+triangle[i][j])
print(max(triangle[n-1]))










