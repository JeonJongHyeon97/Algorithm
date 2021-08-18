import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    # 소수인지 고려할 필요 없음, 앞에서 이미 나눠지므로
    for i in range(2, n + 1):
        cnt = 0
        if n % i == 0:
            while n % i == 0:
                n = n // i
                cnt += 1
            print(i, cnt)
        else:
            if n == 1:
                break