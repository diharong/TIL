N, M= map(int,input().split())

def dfs(depth, li):
    if depth == M:
        for i in li:
            print(i, end=" ")
        print()
        return 
    
    for i in range(1,N+1):
        li.append(i)
        dfs(depth+1, li)
        li.pop()


dfs(0,[])
