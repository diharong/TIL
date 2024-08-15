# import sys
# sys.stdin = open('input.txt')

N = int(input())
switch = list(map(int,input().split()))
student = int(input())

for _ in range(student):
    S, GN = map(int, input().split()) #성별(S)과 번호(GN)

    if S == 1:    # 남학생의 경우
        for j in range(N):         
            if switch[GN-1] or switch[(GN*2)-1] == 1:       
                switch[j] = 0
            else :
                switch[j] = 1

    elif S == 2:
        for k in range(N):
            if switch[(GN-1)-k] == switch[(GN-1)+k] :
                switch2_li = list(switch[(GN-1)-k:(GN-1)+k+1])
                if switch2_li[k] == 0:
                    switch2_li = 1
                else :
                    switch2_li = 0
            else :
                if switch[GN-1] == 0:
                    switch[GN-1] = 1
                else:
                    switch[GN-1] = 0

# N = int(input()) #스위치 개수
# switch = list(map(int,input().split()))
# student = int(input())

# for _ in range(student):
#     S, GN = map(int, input().split()) #성별(S)과 번호(GN)

#     if S == 1:    # 남학생의 경우
#         for j in range(1,N+1):         
#             if j%GN == 0:           
#                 if switch[j-1] == 1:
#                     switch[j-1] = 0
#                 else :
#                     switch[j-1] = 1

#     # 여학생의 경우
#     elif S == 2:
#         if switch[GN-1] == 1:
#             switch[GN-1] = 0
#         else :
#             switch[GN-1] = 1

#         for k in range(1, N):
#             if 0<=(GN-1)-k and (GN-1)+k < N:
#                 if switch[(GN-1)-k] == switch[(GN-1)+k] :
#                     if switch[GN-1-k] == 1:
#                         switch[GN-1-k] = 0
#                         switch[GN-1+k] = 0
#                     else :
#                         switch[GN-1-k] = 1
#                         switch[GN-1+k] = 1
#                 else :
#                     break
#             else:
#                 break
                
# for i in range(N):
#     print(switch[i], end=' ')
#     if (i + 1) % 20 == 0:  # 20개씩 줄 바꿈
#         print()            















# N = int(input())  # 스위치 개수
# switch = list(map(int, input().split()))  # 스위치 상태
# student = int(input())  # 학생 수

# for _ in range(student):
#     S, GN = map(int, input().split())  # 성별(S)과 번호(GN)

#     if S == 1:  # 남학생의 경우
#         for j in range(GN-1, N, GN):  # GN의 배수인 스위치를 변경
#             switch[j] = 1 if switch[j] == 0 else 0

#     elif S == 2:  # 여학생의 경우
#         GN -= 1  # 인덱스를 맞추기 위해 1을 뺌
#         l, r = GN, GN
#         while l >= 0 and r < N and switch[l] == switch[r]:  # 대칭 구간 탐색
#             switch[l] = 1 if switch[l] == 0 else 0
#             if l != r:
#                 switch[r] = 1 if switch[r] == 0 else 0
#             l -= 1
#             r += 1

# # 출력 형태 맞추기
# for i in range(N):
#     print(switch[i], end=' ')
#     if (i + 1) % 20 == 0:  # 20개씩 줄 바꿈
#         print()
