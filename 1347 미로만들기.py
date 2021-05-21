# -*- coding: utf-8 -*-
"""
홍준이는 미로 안의 한 칸에 남쪽을 보며 서있다. 미로는 직사각형 격자모양이고, 각 칸은 이동할 수 있거나, 벽을 포함하고 있다. 
모든 행과 열에는 적어도 하나의 이동할 수 있는 칸이 있다. 홍준이는 미로에서 모든 행과 열의 이동할 수 있는 칸을 걸어다녔다. 
그러면서 자신의 움직임을 모두 노트에 쓰기로 했다. 홍준이는 미로의 지도를 자기 노트만을 이용해서 그리려고 한다.

입력으로 홍준이가 적은 내용이 주어진다. 문자열로 이루어져 있으며, 모든 문자 하나는 한 번의 움직임을 말한다. 
‘F’는 앞으로 한 칸 움직인 것이고, ‘L'과 ’R'은 방향을 왼쪽 또는 오른쪽으로 전환한 것이다. 즉, 90도를 회전하면서, 
위치는 그대로인 것이다.
"""



n = int(input())
move=list(input())
loc=[0,0]
miro_x=[0]
miro_y=[0]
direction = 270
for i in move:
    if i =='R':
        direction=(direction+90)%360
    elif i =='L':
        direction=(direction-90)%360
    elif i =='F':
        if direction == 0:
            loc=[loc[0],loc[1]-1]
            miro_y.append(loc[0])
            miro_x.append(loc[1])
        elif direction == 90:
            loc=[loc[0]+1,loc[1]]
            miro_y.append(loc[0])
            miro_x.append(loc[1])
        elif direction == 180:
            loc=[loc[0],loc[1]+1]
            miro_y.append(loc[0])
            miro_x.append(loc[1])
            
        elif direction == 270:
            loc=[loc[0]-1,loc[1]]
            miro_y.append(loc[0])
            miro_x.append(loc[1])
            
range_x=[min(miro_x),max(miro_x)]
range_y=[min(miro_y),max(miro_y)]

miro = [['#']*(range_x[1]-range_x[0]+1) for _ in range((range_y[1]-range_y[0]+1))]
if range_x[0] <0:
    for i in range(len(miro_x)):
        miro_x[i]+=(0-range_x[0])
if range_y[0] <0:
    for i in range(len(miro_y)):
        miro_y[i]+=(0-range_y[0])        

for i in range(len(miro_x)):
    miro[miro_y[i]][miro_x[i]]="."

for i in range(len(miro)-1,-1,-1):
    print("".join(miro[i]))



            
            