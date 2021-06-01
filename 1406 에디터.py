# -*- coding: utf-8 -*-

#insert 보다 직접 slicing이 더 빠름
#스택을 이용하여 커서를 기준으로 좌,우를 나눔

import sys 
input=sys.stdin.readline
left = list(input()) 
right = []
m = int(input()) 
for _ in range(m): 
    command = input()
    if command[0] == 'L' and left: 
        right.append(left.pop()) 
    elif command[0] == 'D' and right: 
        left.append(right.pop()) 
    elif command[0] == 'B' and left: 
        left.pop() 
    elif command[0] == 'P': 
        left.append(command[-1]) 
    print()
    print(''.join(left + right[::-1]))

print(''.join(left + right[::-1]))
