# -*- coding: utf-8 -*-
"""
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M*N 크기의 보드를 찾았다. 
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 
지민이는 이 보드를 잘라서 8*8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 
각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 
하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8*8 크기의 체스판으로 잘라낸 후에 
몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
"""

#   다중 for문을 이용하여 모든 경우를 확인 -> 그중 최소값 찾기
#   (0,0) (0,1) (0,2)
#   (1,0) (1,1) (1,2)
#   -> 좌표의 합이 홀/짝 인 경우 같은 색
n, m = map(int, input().split())
total = []
result = []

for i in range(n):
    total.append(input())

for total_x in range(n-7):
    for total_y in range(m-7):
        case_B = 0  #첫번째 타일이 B라고 가정
        case_W = 0  #첫번째 타일이 W라고 가정
        for sub_x in range(total_x, total_x + 8):
            for sub_y in range(total_y, total_y + 8):
                if (sub_x + sub_y)%2==0:
                    if(total[sub_x][sub_y]=="W"):
                        case_B +=1
                    if(total[sub_x][sub_y]=="B"):
                        case_W +=1
                else:
                    if(total[sub_x][sub_y]=="B"):
                        case_B +=1
                    if(total[sub_x][sub_y]=="W"):
                        case_W +=1
        result.append(case_B)
        result.append(case_W)
    
print(min(result))



