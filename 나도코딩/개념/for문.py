for waiting_no in [0, 1, 2, 3,4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5): # 0,1,2,3,4
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1,5): # 1,2,3,4,5
    print("대기번호 : {0}".format(waiting_no))


starbucks = ["아이언맨", '토르', "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))


# 리스트 컴프리헨션 사용하기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3) # a에 있는 요소를 하나씩 뽑아서 곱하기 3을 하는데, 이걸 result에 담아준다.
# result 라는 변수가 비어있다. num 에 3을 곱해서, append (추가) 이걸 빈 result에 추가를 해주는 개념.
# 차례로 [3, 6, 9, 12] 가 추가가 된다.

print(result)

#이걸 간략하게 쓰기
a = [1,2,3,4]
result = [num*3 for num in a] # 결과를 먼저 써준다 num*3 , num*3이라는결과를 낼껀데 이걸 어떻게 낼꺼냐
# a를 뽑아서 순회하면서 num 을 만들꺼야
print(result)

# if문도 포함해보기
a = [1,2,3,4]
result = [num*3 for num in a if num % 2 == 0]

# 이걸 풀어쓰면
result = []
for num in a:
    if num % 2 == 0:
        result.append(num*3)

# 하나 더 
result = [x*y for x in range(2,10) for y in range(1,10)]

print(result)

# 이걸 풀어쓰면
result =[]
for x in range(2,10):
    for y in range(1,10):
        result.append(x*y)

print(result)

# 싸피 프로젝트 과정 중 
name_list = []