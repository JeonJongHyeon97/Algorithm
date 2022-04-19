# -*- coding: utf-8 -*-

Str = list(input())
answer = []
for i in range(len(Str)):
    count = 0
    answer.append(Str[i])
    count +=1
    while i-count >= 0 and i+count < len(Str):
        if Str[i-count:i] == Str[i+1:i+count+1][::-1]:
            answer.append("".join(Str[i-count:i+count+1]))
        count+=1
print(sorted(answer,key=lambda x: len(x))[-1])