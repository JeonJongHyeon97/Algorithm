import sys
input=sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    applicant = [0 for i in range(N+1)]
    for __ in range(N):
        a, b = (map(int, input().split()))
        applicant[a] = b
    cri = applicant[1]
    for i in range(2, len(applicant)):
        tmp = applicant[i]
        if tmp>cri:
            N-=1
            continue
        cri = min(cri, tmp)
    print(N)