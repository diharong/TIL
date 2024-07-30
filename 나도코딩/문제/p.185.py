
# customers_num = range(1, 51)

# for time in randomrange(5, 51):
#     if time in customers_num[4:17]:
#         print([0])
#     else:
#         print([1])

# print()

# 진짜 모르겠음 ㅋ 

# from random import *
# count = 0 # 총 탑승 승객수
# for i in range(1, 51): # 1부터 50까지 수 (승객)
#     time = randrange(5, 51) #5~50분 소요시간
#     if 5 <= time <= 15: # 5분~15분 이내의 손님 (매칭성공), 탑승 승객 수 증가 처리
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         count += 1
#     else: # 매칭 실패한 경우
#         print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {0} 분".format(count))


from random import *
customer = 0 # 총 탑승 승객 수 
for i in range(1,51): # 1부터 50까지 승객수
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        customer += 1
    else:
        print("[] {0}번째 손님 (소요시간) : {1}분".format(i, time))

print("총 탑승객 : {0}명".format(customer))


