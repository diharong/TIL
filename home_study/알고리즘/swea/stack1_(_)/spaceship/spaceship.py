import sys
sys.stdin = open("input.txt", "r")

# T = int(input())

# for tc in range(1,T+1):
#     N, M = map(int,input(). split())
#     arr = [list(map(int,input().split()))for _ in range(N)]
           
#     di = [0,1,1,1,0,-1,-1,-1]
#     dj = [1,1,0,-1,-1,-1,0,1]

#     count = 0

#     for i in range(N):
#         for j in range(M):
#             current_point = 0
#             for k in range(len(di)):
#                 ni = i + di[k]
#                 nj = j + dj[k]
#                 if 0<=ni<N and 0<=nj<M:
#                     if arr[i][j] > arr[ni][nj]:
#                         current_point += 1

#             if current_point >=4 :
#                 count += 1

#     print(f'{tc} {count}')



#     # 테스트 케이스 수 T를 입력받음
# T = int(input())

# # 각 테스트 케이스에 대해 실행
# for tc in range(1, T + 1):
#     # 배열의 크기 N (행의 수)와 M (열의 수)를 입력받음
#     N, M = map(int, input().split())
    
#     # N x M 크기의 높이 정보를 입력받아 2차원 리스트(arr)에 저장
#     arr = [list(map(int, input().split())) for _ in range(N)]
    
#     # 8방향(상, 상우, 우, 하우, 하, 하좌, 좌, 상좌)을 나타내는 리스트
#     di = [0, 1, 1, 1, 0, -1, -1, -1]  # 행의 변화량
#     dj = [1, 1, 0, -1, -1, -1, 0, 1]  # 열의 변화량
    
#     # 후보지로 선정된 지역의 개수를 세기 위한 변수 count
#     count = 0

#     # 2차원 배열의 각 셀을 탐색
#     for i in range(N):
#         for j in range(M):
#             # 현재 위치 (i, j)의 후보지 가능성을 판단할 변수
#             current_point = 0
            
#             # 8방향으로 주변을 탐색
#             for k in range(len(di)):
#                 ni = i + di[k]  # 이동할 새로운 행 위치
#                 nj = j + dj[k]  # 이동할 새로운 열 위치
                
#                 # 새로운 위치(ni, nj)가 배열 범위 내에 있는지 확인
#                 if 0 <= ni < N and 0 <= nj < M:
#                     # 현재 위치 (i, j)의 높이가 주변 위치 (ni, nj)보다 큰지 비교
#                     if arr[i][j] > arr[ni][nj]:
#                         current_point += 1  # 주변보다 높으면 current_point 증가
            
#             # 주변 8방향 중 4곳 이상에서 현재 위치가 더 높다면 후보지로 간주
#             if current_point >= 4:
#                 count += 1  # 후보지로 판정된 셀의 개수를 count에 추가

#     # 테스트 케이스 번호와 후보지 개수를 출력
#     print(f'{tc} {count}')




T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    di = [0,1,1,1,0,-1,-1,-1]
    dj = [1,1,0,-1,-1,-1,0,1]

    count = 0
    for i in range(N):
        for j in range(M):
            low_A = 0
            for k in range(len(di)):
                ni = i+di[k]
                nj = j+dj[k]
                if 0<= ni < N and 0<= nj < M:
                    if arr[i][j] > arr[ni][nj]:
                        low_A += 1

            if low_A >= 4:
                count += 1
        
    print(f'#{tc} {count}')