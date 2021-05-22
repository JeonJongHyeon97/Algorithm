
# 수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

# Dynamic programming
# dp[n]=dp[n-1]+dp[n-2]+dp[n-3] 점화식을 이용
# 1463번과 동일한 아이디어


k = int(input())

for _ in range(k):
    n = int(input())
    
    dpList=[0,1,2,4]
    for i in range(4, n+1):
        if i >=4:
            dpList.append(dpList[i-1] + dpList[i-2] + dpList[i-3])
    print(dpList[n])
    
    

    


