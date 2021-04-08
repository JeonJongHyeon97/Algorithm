# -*- coding: utf-8 -*-
"""
나이트 투어는 체스판에서 나이트가 모든 칸을 정확히 한 번씩 방문하며, 
마지막으로 방문하는 칸에서 시작점으로 돌아올 수 있는 경로이다. 
다음 그림은 나이트 투어의 한 예이다.

영식이는 6×6 체스판 위에서 또 다른 나이트 투어의 경로를 찾으려고 한다. 
체스판의 한 칸은 A~F 중의 알파벳 하나와 1~6 중의 숫자 하나로 나타낼 수 있다. 
영식이의 나이트 투어 경로가 주어질 때, 이것이 올바른 것이면 Valid, 
올바르지 않으면 Invalid를 출력하는 프로그램을 작성하시오.

"""
# 알파벳+숫자 좌표를 숫자+숫자 좌표로  변경후, 입력 값이 이전의 값에서 나이트의 움직임이 맞는지
# 이전에 나왔던 좌표가 아닌지 확인

abc=["A","B","C","D","E","F"]
history=[]

move=input()
move_x=str(abc.index(move[0])+1)
move_y=move[-1]
first = move_x+move_y
history.append(first)
error = False
for i in range(35):
    move=input()
    move_x=str(abc.index(move[0])+1)
    move_y=move[-1]
    if ((move_x+move_y) in history) or (int(history[i][1])-int(move_y))==0 or (int(history[i][0])-int(move_x))==0 or (int(history[i][1])-int(move_y))/(int(history[i][0])-int(move_x)) not in [2, -2, 0.5, -0.5]:
        error=True
    history.append(move_x+move_y)
    
history=list(set(history))
if (len(history)!=36) or (error) or (int(history[-1][1])-int(first[1]))==0 or (int(history[-1][0])-int(first[0]))==0 or (int(history[-1][1])-int(first[1]))/(int(history[-1][0])-int(first[0])) not in [2, -2, 0.5, -0.5]:
    print("Invalid")
else:
    print("Valid")


    
    
    
    
    
    
