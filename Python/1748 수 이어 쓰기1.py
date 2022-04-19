import sys
input = sys.stdin.readline




n = input().rstrip()    # 120
a = len(n)  # 3
answer=0
for i in range(1,a):
    answer += (a-i)*(10**int(a-1-i)*9)
answer+=a*(int(n)-10**(a-1)+1)
print(answer)
