import sys
sys.stdin = open("input.txt", "r")


# 수정 전 코드
# T = int(input())

# for tc in range(1, T+1):
#     N, K = map(int,input().split())
#     arr_K = list(map(int, input().split()))

#     li_N = []
#     Not_K =[]

#     for i in range(N):
#         li_N = li_N.append(i)
#         for j in arr_K:
#             if j not in li_N:
#                 Not_K.append(j)

#     print(f'{tc} {Not_K}')


T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr_K = list(map(int, input().split()))

    li_N = list(range(1,N+1))
    Not_K =[]

    for i in li_N:
        if i not in arr_K:
            Not_K.append(i)

    result = ' '.join(map(str, Not_K))
    print(f'{tc} {result}')
