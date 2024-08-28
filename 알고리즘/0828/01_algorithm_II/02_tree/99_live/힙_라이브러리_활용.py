'''
7
20 15 19 4 13 11 17

7
20 15 19 4 13 11 23
'''


from heapq import heappush, heappop

N = int(input())          # 필요한 노드 수
arr = list(map(int, input().split()))

heap = []  # 최대힙을 구현하기 위한 리스트

# 최소힙 ( 기본 )
for num in arr:
    heappush(heap, num)     

print([x for x in heap])  # 힙의 내부 상태를 출력 (음수로 저장된 상태)

while heap:
    print(heappop(heap), end=' ')

print('\n------------------------------------')

# 최대힙
# 삽입 시 음수로 곱하여 저장 (제일 큰 수가 제일 작아짐)
# 삭제 후 음수값을 곱하여 출력 (다시 원래 수로 복구하여 출력)
for num in arr:
    heappush(heap, -num)

print([-x for x in heap])  # 힙의 내부 상태를 출력 (음수로 저장된 상태)

while heap:
    print(-heappop(heap), end=' ')


# 튜플형태일 때 우선순위를 주고 싶은 데이터를 앞에다 배치

'''
1. BST, 힙 그림으로 이해하기 ✨
2. 코드 이해하기
3. heap q 라이브러리 활용해보기
'''