import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    Ai = list(map(int,input().split()))
    Bj = list(map(int,input().split()))

    
    max_value = float('-inf')   # 음수 무한대

    diff = len(Bj)-len(Ai) 

    for i in range(abs(diff)+1):
        S = 0
        if diff > 0:
            for j in range(len(Ai)):
                S += Ai[j]*Bj[j+i]

        else :
            for j in range(len(Bj)):
                S += Bj[j]*Ai[j+i]

        # if i == 0:
        #     max_value = sum

        if max_value < S:
            max_value = S

    print(f'#{tc} {max_value}')

    
        



              