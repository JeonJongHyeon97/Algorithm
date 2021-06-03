from itertools import combinations_with_replacement
n, m = map(int, input().split())
num = list(map(int,input().split()))
output=[]
for i in combinations_with_replacement(num,m):
    output.append(sorted(list(i)))

for i in sorted(output):
    print(*i)



