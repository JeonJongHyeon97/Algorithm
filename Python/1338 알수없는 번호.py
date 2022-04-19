# -*- coding: utf-8 -*-
"""
당신은 한 개의 알 수 없는 수를 알아내야만 한다. "이런 젠장"

어쨌든 당신은 그 수를 알아내야만 한다. 당신에게 주어지는 정보는 다음과 같다.

1. 그 수가 있을 수 있는 범위
2. 그 수를 x로 나눈 나머지, 즉 그 수를 qx + y(0 ≤ y < |x|) 꼴로 나타냈을 때 y의 값
이때, 당신은 그 수가 무엇인지 추측해야 한다.
"""

start, end = map(int, input().split() )
x, y = map(int, input().split() )
answer=[]
if end-start > x :
    print("Unknwon Number")
else:
    for i in range(start, end+1):
        if(i%x==y):
            if len(answer) <2:
                answer.append(i)
            else:
                print("Unknwon Number")
                break
    print(answer[0])
    
    
    
