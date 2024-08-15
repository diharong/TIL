import sys
sys.stdin = open("input.txt", "r")

# 아놔 이코드 테케 10개중에 5개만 맞음
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     C_li = list(map(int,input().split()))

#     # print(C_li) 결과 값 헷갈려서 프린트 해봄
    
    
#     max_len = 1     # 연속한 숫자 묶음 최대 길이 최솟값은 1
#     current_len = 1 # 현재 묶음 길이 # 처음에 0으로 설정해서 테케 하나가 안맞았음
#     # 0으로 설정하면 안되는 이유 = 당근이 하나라도 있으면 그 당근의 묶음 길이는 최소 1이 되어야하니까!!바보냐


#     for i in range(N-1):        # 처음에 N으로 설정해서 list index out of range가 났음
#         if C_li[i+1] == C_li[i] + 1:    # N으로 설정하면 i+1 이 범위를 넘어가버림 
#             current_len += 1
#         else : 
#             current_len = 1

#         if max_len < current_len:
#             max_len = current_len
            
            
#     print(f'#{tc} {max_len}')   
    
    


'''
처음에는 리스트를 만들어서 연속된 숫자들을 집어넣으려고 했는데 
접근이 잘못된 듯 
진행이 어려웠음

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C_li = list(map(int,input().split()))

    result = []
    for i in range(N-1)
        if C_li[i+1] == C_li[i] + 1:
            result.append(C_li[i])
            result.append(C_li[i+1])
여기까지 생각했는데 막혔음!!! ㅠㅠ 

# '''



#     #error : list index out of range 

#     # 나도 함수 쓰고 싶어!!!


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     C_li = list(map(int,input().split()))

#     # print(C_li) 결과 값 헷갈려서 프린트 해봄
    
    
#     max_len = 1     # 연속한 숫자 묶음 최대 길이 최솟값은 1
#     current_len = 1 # 현재 묶음 길이 # 처음에 0으로 설정해서 테케 하나가 안맞았음
#     # 0으로 설정하면 안되는 이유 = 당근이 하나라도 있으면 그 당근의 묶음 길이는 최소 1이 되어야하니까!!바보냐


#     for i in range(1, N):        # (1,N) 왜 1부터 시작해 
#         if C_li[i] == C_li[i-1] + 1:    # 음 왜 아까꺼랑 다른게 먼디
#             current_len += 1
#         else : 
#             current_len = 1

#         if max_len < current_len:
#             max_len = current_len
            
            
#     print(f'#{tc} {max_len}')  

    # 테케가 왜 10개중에 5개만 맞는거야야아아ㅏ아아아앙 
    

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     C_li = list(map(int,input().split()))

#     # print(C_li) 결과 값 헷갈려서 프린트 해봄
    
    
#     max_len = 1     # 연속한 숫자 묶음 최대 길이 최솟값은 1
#     current_len = 1 # 현재 묶음 길이 # 처음에 0으로 설정해서 테케 하나가 안맞았음
#     # 0으로 설정하면 안되는 이유 = 당근이 하나라도 있으면 그 당근의 묶음 길이는 최소 1이 되어야하니까!!바보냐


#     for i in range(N-1):        # 처음에 N으로 설정해서 list index out of range가 났음
#         if C_li[i+1] > C_li[i]:    # N으로 설정하면 i+1 이 범위를 넘어가버림 
#             current_len += 1
#         else : 
#             current_len = 1

#         if max_len < current_len:
#             max_len = current_len
            
            
#     print(f'#{tc} {max_len}')


# # 연속된 수를 출력
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     C_li = list(map(int,input().split()))

#     num_list = []  
#     result = [] # 최대 배열을 담아줄 리스트


#     for i in range(N):
#         if i == 0:
#             num_list.append(C_li[i])
#             continue 

#         if C_li[i] > C_li[i-1]:
#             num_list.append(C_li[i])
#         else:
#             num_list = []
#             num_list.append(C_li[i])

    
#         if len(result) < len(num_list):
#                 result = num_list

#     print(result)

        
            

   