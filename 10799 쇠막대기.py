# -*- coding: utf-8 -*-

pipe = list(input())
total=0
stack=0



for i in range(0, len(pipe)):
    # print(" ")
    # print(pipe[i])
    # print(pipe[i:i+2]==['(',')'])
    if pipe[i:i+2]==['(',')']:
        total+=stack
    elif i>=1 and pipe[i-1:i+1]==['(',')']:
        continue
    else:
        if pipe[i] =='(':
            stack+=1
        elif pipe[i] == ')':
            stack-=1
            total+=1
            
    # print("stack : ", stack)
    # print("total : ", total)
print(total)  
        
        