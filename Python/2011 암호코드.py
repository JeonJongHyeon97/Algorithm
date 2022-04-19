import sys
input=sys.stdin.readline
n = list(map(int,input().strip()))
dp = [0 for _ in range(len(n)+1)]
if n[0] == 0:
    print(0)
else:
    dp[1]=1
    for i in range(1, len(n)):
        if n[i] == 0:
            if n[i-1] == 0:
                continue
        if 10 <= (n[i - 1] * 10 + n[i]) < 27:
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]
    print(dp)
    print(dp[len(n)-1]%1000000)