# 스위치 켜고 끄기 
'''


>> 




^_____^
'''

import sys
sys.stdin = open('input.txt')


'''
IM 이런식이면 쫌 곤 란 하 다 .
'''
'''
how?
1. 남학생과, 여학생의 케이스로 나누자
2. 남학생의 경우 스위치의 개수만큼 순회하면서,
    만약에 스위치번호가 자기가 받은 수의 배수이면, 스위치의 상태를 바꾼다.
    ==> '만약에 스위치번호가 자기가 받은 수의 배수이면' 를 처리를 안햇네 하하
    스위치 상태만 바꿔버림ㅠ3ㅠ

3. 여학생의 경우, 받은 수의 스위치를 중심으로 스위치 상태가 대칭이면 스위치 상태 바꿈
    대칭이 아니면 자기자신만 바꿈 
    => 어쨌든 자기자신은 항상 바뀌는 것 -> 실제 문풀에서는 이걸 적용 못함.! 

'''
'''
<후기>
1. 문제분석 - 처음에는 문제 이해도 잘 안됐었는데 하나하나 씹어먹으니 문제가 이해되기 시작 - 시간에 쫓기지말고 천천히 분석해보자!
2. how ? - 어떻게 구현을 해야할지 조금 막막했음, 근데 찬찬히 문제를 다시보고선 큰 카테고리로 경우의 수를 나누어보았다. 남,여 학생 이런식
            규칙을 찾아내는 거-- 중요한 것 같다. 
            for 문 쓸 때 범위를 찾는 거 아직 미숙한 것 같다.
            문제에 나오는 조건들을 다 적용하는 거 힘든 것 같고, 특히! 여학생의 경우, 자기자신이면 항상 스위치상태가 바뀐다. 와 같은 
            부분을 생각해내는게 훈련이 필요할 것 같다. 
3. 논리가 한번 꼬이니 중간에 추가해야할 조건을 생각해내도 어느 코드 사이에 넣어야하는지 젤 막막했다. -- 이 훈련은 어케 하나요?~?~?~?
4. 코드를 완성하고 보니 쉬운듯,,, 하면서 꼼꼼하게 따지지 않으면 멸망의 길로 가기 쉽상임을 깨달음. 
5. 그래도 뭔가 구현을 해보았다는 거에 큰 성장을 느꼈다 ^ㅡㅡ^ 너무 긍정적 이거맞냠스 ㅎ , ㅎ
6.
'''
# 처음 풀었을 때 코드 
N = int(input())
switch = list(map(int,input().split()))
student = int(input())

for _ in range(student):   
    S, GN = map(int, input().split()) #성별(S)과 번호(GN)

    if S == 1:    # 남학생의 경우
        for j in range(N):                                  # GN-1 로 한 이유는 스위치의 번호와 인덱스가 1차이 나기 때문에!
            if switch[GN-1] or switch[(GN*2)-1] == 1:     # 만약에 자기가 받은 수 또는 배수의 스위치 상태가 1이면 (주석을 달면서 먼가 이상하다는 것을 깨달았습니다..스앵님)
                switch[j] = 0                               # 0으로 바꾸고
            else :
                switch[j] = 1                           # 아니면 1로 바꾼다.

    elif S == 2:    # 여학생의 경우
        for k in range(N):
            if switch[(GN-1)-k] == switch[(GN-1)+k] :   # 만약에 스위치의 양쪽 대칭 값이 같다면
                switch2_li = list(switch[(GN-1)-k:(GN-1)+k+1])  # 그 값들을 리스트에 담는다. 지금생각하니 왜 담았지 ?? 싶음. 문제 이해를 잘못한듯 
                if switch2_li[k] == 0:                          # 여기 밑에서 부터 논리가 다 꼬여버린 ,,것이,,옵니다.
                    switch2_li = 1
                else :
                    switch2_li = 0
            else :                                      # 만약에 스위치의 양쪽 대칭 값이 같지 않다면 
                if switch[GN-1] == 0:
                    switch[GN-1] = 1
                else:
                    switch[GN-1] = 0






# 재도전 - 근데 지피티행님과 친구의 도움을 받음 ,,^_^
N = int(input()) #스위치 개수
switch = list(map(int,input().split()))
student = int(input())

for _ in range(student):
    S, GN = map(int, input().split()) #성별(S)과 번호(GN)

    if S == 1:    # 남학생의 경우
        for j in range(1,N+1):         # for 문 범위 설정하는게 아직 미숙해염,,,
            if j%GN == 0:             # 배수를 표현하는 방법 수정.
                if switch[j-1] == 1:
                    switch[j-1] = 0
                else :
                    switch[j-1] = 1

    # 여학생의 경우
    elif S == 2:
        if switch[GN-1] == 1:     # 자기자신의 스위치는 항상 변경되어야한다. 라는 조건 추가
            switch[GN-1] = 0
        else :
            switch[GN-1] = 1

        for k in range(1, N):       
            if 0<=(GN-1)-k and (GN-1)+k < N:            # 이 범위도 설정안해줬었음! 인덱스 에러 방지
                if switch[(GN-1)-k] == switch[(GN-1)+k] :   # 인덱스 값들이 대칭이면
                    if switch[GN-1-k] == 1:                     # 1 이면 대칭 값들을 0으로 바꿔주고
                        switch[GN-1-k] = 0                      
                        switch[GN-1+k] = 0
                    else :                                      # 1이 아니면 대칭 값들을 1로 바꿔준다. 
                        switch[GN-1-k] = 1
                        switch[GN-1+k] = 1
                else :
                    break                                   # 인덱스 값들이 대칭이 아니면 break 위에서 자기자신은 항상 바뀐다는 조건을 걸어줘서 break해도됨
            else:
                break                                       # 대칭 범위가 인덱스 범위를 넘어가면 걍 중지. 
                
for i in range(N):
    print(switch[i], end=' ')
    if (i + 1) % 20 == 0:  # 20개씩 줄 바꿈                 # 이건 방식을 아예 몰랐다. 외워야겠다!
        print()            








# 이건 지피티 행님 코드 - 근데 while문 적응이 안된 상태라 활용 못함 이슈. 
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
