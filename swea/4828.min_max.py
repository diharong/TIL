T = int(input())

for tc in range(1, T+1):        #michin range안적었음
    N=int(input())
    arr = list(map(int,input().split()))

    min_num = arr[0]
    max_num = arr[0]

    for i in arr:
        if max_num < i:
            max_num = i
        if min_num > i:
            min_num = i

    print(f"#{tc} {max_num - min_num}")