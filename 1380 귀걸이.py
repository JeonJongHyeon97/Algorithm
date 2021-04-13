# -*- coding: utf-8 -*-
"""
파스칼 고등학교에 다니는 많은 여학생들은 규정에 없는 귀걸이를 착용한 채 도망다닙니다. 
Sneddon 교감선생님은 흔들거리는 긴 빨간 귀걸이들을 볼때마다 압수합니다.

교감선생님은 귀걸이를 압수당한 여학생들을 숫자를 매겨 리스트를 작성하고 있습니다. 
그리고 압수한 귀걸이 뒤쪽에 여학생 번호와 마음대로 선택한 'A' 또는 'B'를 함께 적어두었습니다.

모든 정규 일과와 방과후 수업의 감금이 끝나면, 여학생들은 교감선생님을 찾아와 귀걸이를 돌려받습니다. 
불행하게도 어느 날, 교감선생님은 귀걸이가 든 봉투를 잃어버렸고, 하나를 끝내 찾지 못했습니다.

귀걸이를 받지 못해 화난 소녀의 이름을 교감선생님께 알려주세요.
"""

#   시나리오를 나눠서 저장해주는 것에 주의
#   번호가 두번등장하면 받아가는 걸로 처리

student_num = []
senario = 0
answer=[]
student=[]



while True:
    enter = input()
    if enter == "0":
        student=list(filter(lambda x: x !="removed", student))
        if len(student)>=1:
            answer.append(str(senario)+" "+(" ".join(student)))
        break
    elif len(enter)<=3 and (" " not in enter):
        student=list(filter(lambda x: x !="removed", student))
        if len(student)>=1:
            answer.append(str(senario)+" "+(" ".join(student)))
        senario+=1
        student=[]
        student_num = []
    elif len(enter)>3:
        student.append(enter)
    elif " B" in enter or " A" in enter:
        if (enter[:-2] in student_num):
            student.pop(int(enter[:-2])-1)
            student.insert(int(enter[:-2])-1, "removed")
        else:
            student_num.append(enter[:-2])
            
for i in range(1,len(answer)):
    print(answer[i])