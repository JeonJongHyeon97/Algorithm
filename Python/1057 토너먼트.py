# -*- coding: utf-8 -*-

# 번호가 매겨지는 규칙 찾기
# 둘의 번호가 같아지는 라운드에서 return


n, a, b = map(int, input().split())

def starcraft(a: int, b: int, num: int, Round: int):
    if a==b:    # same number
        print(Round-1)
        return
    a=(a+1)//2  # next round number
    b=(b+1)//2  # next round number
    starcraft(a, b, (num+1)//2, Round+1)

starcraft(min(a,b),max(a,b),n,1)







