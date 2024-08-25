T = int(input())
for tc in range(1, T+1):
    N,K = map(int,input().split())

    result = 0

    def dfs(depth, sum):
        global result
        if depth == N:
            if sum == K:
               result += 1   
            return 
        
        
        for i in range(1,13):
            sum += i
            dfs(depth+1, sum)
            sum -= i

    dfs(0,0)
    print(result)

# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())

#     def dfs(depth, sum):
#         if depth == N:
#             if sum == K:
#                 return 1
#             return 0
        
#         count = 0
#         for i in range(1, 13):
#             count += dfs(depth + 1, sum + i)
        
#         return count

#     result = dfs(0, 0)
#     print(result)
