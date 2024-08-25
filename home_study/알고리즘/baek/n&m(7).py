N, M = map(int,input().split())
N_li = list(map(int,input().split()))
N_li.sort()

def dfs(depth, li):
    if depth == M:
        for i in li:
            print(i, end=" ")
        print()
        return

    for i in range(N):
        li.append(N_li[i])
        dfs(depth+1, li)
        li.pop()

dfs(0, [])