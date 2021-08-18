import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())
answer = 0
while n > 0:
    mid = (2 ** n) // 2
    if n > 1:
        if mid > r and mid <= c: # 2사분면
            answer += mid ** 2
            c -= mid
        elif mid <= r and mid > c: # 3사분면
            answer += (mid ** 2) * 2
            r -= mid
        elif mid <= r and mid <= c: # 4사분면
            answer += (mid ** 2) * 3
            r -= mid
            c -= mid
    elif n == 1: # 마지막 위치
        if r == 0 and c == 1:
            answer += 1
        elif r == 1 and c == 0:
            answer += 2
        elif r == 1 and c == 1:
            answer += 3
    n -= 1
print(answer)