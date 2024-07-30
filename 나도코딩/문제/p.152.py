'''
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 신청하기로 함
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됨
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample 을 활용

# '''


# from random import *
# st = [1,2,3,4,5]
# print(st) # 원본 리스트 출력
# shuffle(st) # 리스트 섞기
# print(st) # 섞은 후 리스트 출력
# print(sample(st, 1)) # 리스트에서 값 1개를 무작위로 뽑기


# from random import *

# id = int((random()*20) +1)
# print(id)
# shuffle(id)
# print(id)
# print(sample(id,1))
# print("-- 당첨자 발표" "치킨 당첨자 : ")

from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
# 하지만 range는 리스트가 아니여서 리스트로 형변환해야댐
users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피

print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")