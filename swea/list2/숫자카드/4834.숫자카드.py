# import sys
# sys.stdin = open("input.txt", "r")

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int,input()))

#     # max_value = max(arr)
#     # result = arr.count(max_value)

#     # print(f'#{tc} {max_value} {result}')



# 큐~ 암호생성~
for tc in range(1,11):
    tc = int(input())
    
    num = list(map(int, input().split()))
    
    while num[-1] > 0:
        for i in range(1,6):
            hair = num[0]-i
            num.pop(0)
            num.append(hair)
            
            if num[-1]<=0:
                num[-1] = 0
                break

    
    print(*num)