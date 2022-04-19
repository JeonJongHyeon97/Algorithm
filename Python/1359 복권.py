# -*- coding: utf-8 -*-
"""
어제, 지민이는 몰래 리조트에 갔다가 입구에 걸려있는 복권 광고를 하나 보았다.

“1부터 N까지의 수 중에 서로 다른 M개의 수를 골라보세요. 저희도 1부터 N까지의 수 중에 서로 다른 M개의 수를 고를건데, 적어도 K개의 수가 같으면 당첨입니다.!”

지민이는 돌아오면서 자신이 복권에 당첨될 확률이 궁금해졌다.

지민이가 복권에 당첨될 확률을 구하는 프로그램을 작성하시오.
"""

# 확률, 조합으로 해결

import math
def combination(m, n):
    result = math.factorial(m)//math.factorial(n)//math.factorial(m-n)
    return result
n, m, k = map(int, input().split())
answer=0
while(k<=m):
    if(n-m) >= (m-k):
        answer+=combination(m,k)*combination(n-m,m-k)/combination(n,m)
    k+=1
print(answer)
combination(n, m)*combination(m,k)*combination(n-m,m-k)/(combination(n,m)**2)
# ((combination(n, k) * combination(n, m-k))/combination(n,m))**2











