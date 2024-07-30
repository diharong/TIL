# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
 

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python.replace("Python", "Java"))

# print(python.find("Java")) #원하는 값이 없을 때 -1 을 냄
# print(python.index("Java")) #원하는 값이 없을 때 오류를 냄

# print(python.count("n"))

python = "Python is Amazing"

find = python.find("n") # 처음 발견한 n의 인덱스
print(find) # 'Python' 에서 n (인덱스 5)
find = python.find("n", find + 1) # 인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스
print(find) # 'is Amazing' 에서 n(인덱스 15)
find = python.find("Java") # Java 가 없으면 -1 을 반환(출력) 한 후 프로그램 계속 수행
print(find)

index = python.index("n") # 처음 발견한 n의 인덱스
print(index) # 'Python'에서 n
index = python.index("n", index + 1) # 인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스
print(index) # ' is Amazing' 에서 n 
index = python.index("n", 2, 6) # 인덱스 2부터 6 직전까지 찾아 처음 발견한 n의 인덱스
print(index) # 'thon'에서 n(인덱스 5)
index = python.index("Java") # Java가 없으면 오류가 발생하며 프로그램 종료
print(index)

