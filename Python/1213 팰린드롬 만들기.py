# -*- coding: utf-8 -*-
"""
임한수와 임문빈은 서로 사랑하는 사이이다.

임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에, 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.

임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.

임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.
"""

name = list(input())
answer=[]
odd=[]
for i in name:
   if name.count(i)%2 ==1:
       if i*name.count(i) not in odd:
           odd.append(i*name.count(i))

   else: 
       if i not in answer:
           for j in range(name.count(i)//2):
               answer.append(i)
answer=sorted(answer)
       
if len(odd)>1:
    print("I'm Sorry Hansoo")
else:
    print("".join(answer+odd+answer[::-1]))


