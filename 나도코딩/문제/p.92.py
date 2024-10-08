'''
연산자를 이용해 온도 단위를 변환하는 프로그램을 만들어 보세요

조건)
1. 섭씨 온도를 저장하기 위한 변수를 만든다.
2. 다음 공식을 이용해 섭씨 온도를 화씨 온도로 변환하고 새로운 변수에 저장한다.
    화씨 온도 =(섭씨 온도*9/5) +32
3. 섭씨 온도와 화씨 온도를 다음과 같이 출력한다.

# 섭씨 온도가 30도 일때
섭씨 온도 : 30
화씨 온도 : 86.0

# 섭씨 온도가 10도 일 때
섭씨 온도 : 10
화씨 온도 : 50.0
'''
# sub = a
# ha = (a*9/5) + 32 

# a = 30
# print("섭씨 온도 :", a)
# print("화씨 온도 :", ha)

# 문제 풀이

celsius = 30
fahrenheit = (celsius* 9//5) +32
# print("섭씨 온도 : ", celsius) #celsius 는 정수형 이기 때문에 문자열끼리만 결합할 수 있어서 에러남
print("섭씨 온도 : " + str(celsius))
print("화씨 온도 : " + str(fahrenheit))
