# 그래비티 강사님 추천띵크
'''
그래비티

한글 코딩

1. 테스트케이스 입력받기
2. 테스트케이스만큼 순회하기
	3. 방의 가로길이 = N 을 입력받기
	4. 쌓여있는 상자의 수를 리스트형태로 입력받기

	5. max_fall 낙차 최대값을 저장할 변수
	
	6. 각 빌딩의 인덱스를 순회
		7. 자신보다 큰 빌딩의 인덱스를 셀 변수 추가
		8. 각 빌딩의 오른쪽을 순회
			9. 만약에 현재 인덱스의 값보다 오른쪽 인덱스가 같거나 크면(낙차발생하므로)
				10. 현재 보다 큰 빌딩의 개수 추가

		10.낙차값은 가로길이 (N-1) 에서 10번의 현재보다 큰 빌딩의 개수를 빼고 자기자신의 인덱스도 뺌

		11. 만약 max_fall이 10번 낙차값보다 작을 시
			12. max_fall 가 맥스 낙차값이 됨

	13. 출력 
'''


import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    max_fall = 0


    for index in range(N):
        count = 0
        for j in range(index+1, N):
            if arr[index] <= arr[j]:
                count += 1
        
        fall = N-1 - count - index

        if max_fall < fall:
            max_fall = fall
    
    print(f'#{tc} {max_fall}')