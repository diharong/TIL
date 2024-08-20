import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))

    cnt = 0

    for i in range(N):
        if li[i] == 1:
            cnt += 1
            for j in range(i, N, i+1):
                li[j] = 1 - li[j]

    print(cnt)

