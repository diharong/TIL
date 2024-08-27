import sys
sys.stdin = open('input.txt')


def search(node):
    global cnt
    if node != 0:
        cnt += 1
        search(tree[node][0])    
        search(tree[node][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int,input().split()) # E = 간선개수 
    arr = list(map(int,input().split())) #  부모 자식 노드 번호 쌍

    cnt = 0
    tree = [[0, 0] for _ in range(E+2)]

    for i in range(len(arr)//2):
    
        parent = arr[i*2]
        child = arr[i*2+1]
        
        if tree[parent][0] == 0:    
            tree[parent][0] = child
        else:                       
            tree[parent][1] = child
    search(N)
    print(f'#{tc} {cnt}')
    


