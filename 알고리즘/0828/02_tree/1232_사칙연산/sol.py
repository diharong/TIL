import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    # node 번호 인덱스로 사용할 값만 int 로 형변환 해서 tree 정보 기록
    arr = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    arr.insert(0,0) # 0번 노드는 사용하지 않을 것이므로, 0번째에 안쓸 값 삽입
    print(arr)
