# 이진 검색

N = int(input())
key = int(input())
arr = list(map(int,input().split()))

def binarySearch(arr, N, key):

    star = 0
    end = N-1
    while start < =end:
        middle = (start+end)//2
        if arr[middle] == key: # 검색 성공 
            return True
        elif arr[middle] > key :
            end = middle -1
        else:
            start = middle+1
    return False                # 검색 실패


print(binarySearch(arr, N, key))


# 버블정렬
# - 뜻 : 인접한 두 원소들을 비교하여 자리를 계속 교환하는 방식
# - 정렬과정
#     - 첫번째 원소부터 인접한 원소끼리 계속 자리를 바꿔가며
#         맨 마지막 자리까지 이동
#     - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
# - 시간 복잡도 : O(n제곱)

# 구현 
def BubbleSort(arr, N):       #a는 정렬할 리스트, N은 원소의 개수
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



# 풍선팡2
T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_value = 0
    for i in range(N):
        for j in range(M):
            S = arr[i][j]
            for k in range(len(di)):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<= ni < N and 0<= nj < M:
                    S += arr[ni][nj]

            if max_value < S:
                max_value = S
    
    print(f'{max_value}')


# 마법사

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
K = int(input())

di = [-1, 1, 1, -1]
dj = [1, 1, -1, -1]

max_value = 0
for i in range(N):
    for j in range(N):
        S = 0
        for e in range(len(di)):
            for k in range(1, K+1):         # 범위 주의!!!!!!!
                ni = i + di[e]*k 
                nj = j + dj[e]*k 
                if 0<=ni<N and 0<=nj<N : 
                    S += arr[ni][nj]

            if max_value < S :
                max_value = S
    
print(f'{max_value}')
