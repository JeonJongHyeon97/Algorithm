import sys
input = sys.stdin.readline
wooseok = int(input())
dp = [0 for i in range(wooseok+1)]
turn=["SK", "CY"]
if wooseok >3:
    dp[1]="SK"
    dp[2]="CY"
    dp[3]="SK"
    for i in range(4,wooseok+1):
        if dp[i-1] == "SK" or dp[i-3]=="SK":
            dp[i] = "SK"
        else:
            dp[i] = "CY"
    print(dp[wooseok])
else:
    dp=[0, "SK","CY","SK"]
    print(dp[wooseok])





