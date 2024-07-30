cabinet = {3:"유재석", 100 :"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# # print(cabinet.get(3))
# # print(cabinet[5]) 
# # print("hi") # 오류가 뜨고 프로그램 종료됨

# print(cabinet.get(5))
# print("hi") # None 이 뜨고 다음 프로그램 실행

# print(cabinet.get(5))
# print(cabinet.get(5, "사용 가능")) # 없는 키를 실행시키고 싶은 경우 추가 가능
# print("hi")

# print(3 in cabinet) #True 
# print(5 in cabinet) #False

cabinet = {"A-3" : "유재석", "B-100":"김태호"}
# print(cabinet["A=3"])

# 새손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["c-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)