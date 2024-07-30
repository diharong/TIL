# Quiz) 변수를 이용하여 다음 문장을 출력하시오.

# 변수명
# : station 

# 변수값
#  : "사당", "신도림", "인천공항" 순서대로 입력

#  출력 문장
#  : xx 행 열차가 들어오고 있습니다.

station = "사당"
station = "신도림"
station = "인천공항"
print(station, "행 열차가 들어오고 있습니다.")

print((3>0) and (3<5))

print(round(3.14, 1))

from math import *
print(floor(4.99))
print(ceil(3.14))
print(sqrt(4))

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random()*10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random()*10)) # 0~10 미만의 임의의 값 생성
print(int(random()*10) +1) #1 이상 11 미만의 임의의 값 생성 (random()결과를 정수로 변환해 1을 더함)

print(randrange(1, 45)) 
print(randint(1,45))