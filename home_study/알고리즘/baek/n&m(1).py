N, M = map(int,input().split())

visited = [0]*(N+1)
# print(visited)
def dfs(depth, li):
    if depth == M:
        for i in li:
            print(i, end=" ")
        print()
        return
    
    for i in range(1, N+1):
        
        if visited[i] == 0:
            li.append(i)    #골랐다.
            visited[i] = 1 #방문표시
            dfs(depth+1, li)    #그다음수고르러
            li.pop()    #원상복구
            visited[i] = 0

dfs(0,[])            