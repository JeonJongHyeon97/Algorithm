
# 0과 1이 출력되는 경우도 피보나치 수열을 따른다.
# n이 40이하의 숫자이므로 미리 40까지의 피보나치수열을 만든 후 출력한다.
# n이 제한이 없을 경우는 고려하지 못함

t = int(input())
fiboList=[0,1,1]
for i in range(3, 41):
    fiboList.append(fiboList[i-1]+fiboList[i-2])
    
for _ in range(t):
    n=int(input())
    if n==0:
        print("1 0")
    elif n==1:
        print("0 1")
    else:
        print(fiboList[n-1], fiboList[n])


















