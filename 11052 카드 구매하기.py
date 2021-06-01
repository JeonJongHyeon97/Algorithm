'''
i 장을 만들수 있는 경우의 수는 (1,i-1), (2,i-2), ..., (i-2,2), (i-1, 1)
Dynamic Programming 이용
'''

n = int(input())
price = list(map(int, input().split()))
price.insert(0,0)

dp=price.copy() # 처음 넣은 가격을 초기 값으로 지정

if n > 1:
    for i in range(2, n+1): # (1,i-1), (2,i-2), ..., (i-2,2), (i-1, 1)을 위해
        for j in range(1, i//2+1):  # (k, i-k) == (i-k, k) 이므로
            dp[i]=max(dp[i],dp[j]+dp[i-j])  # 점화식
print(dp[n])
