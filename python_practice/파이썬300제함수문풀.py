# #196
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# for i in ohlc[1:4]:
#     if i[-1] > 150:
#         print(i[-1])


# #197
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# for i in ohlc[1:4]:
#     if i[-1] >= i[0]:
#         print(i[-1])

# #198
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# volatility = []
# for i in ohlc[1:4]:
#     a = i[1] - i[2]
#     volatility.append(a)
# print(volatility)

#199
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# for i in ohlc[1:]:
#     if i[0] < i[-1]:
#         print(i[1] - i[2])
#
# #200
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# result = 0
# for i in ohlc[1:]:
#     result += (i[-1] - i[0])
#
# print(result)

# # #201 ~ 203
# def print_coin():
#     for _ in range(100):
#         print("비트코인")
#

# print_coin()
#
# for _ in range(100):
#     print_coin()


# def print_with_smile(a):
#     print(a + ":D")
#
# # print_with_smile("안녕하세요")
#
# def print_upper_price(price):
#     print(price*130%)
#
#
# def print_sum(a,b):
#     print(a+b)

# def print_a_o(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)

# #220
# def print_max(a,b,c):
#     check = 0
#     if check < a:
#         check = a
#     if check < b:
#         check = b
#     if check < c:
#         check = c
#     print(check)
#
# print_max(3,5,4)

#221
# def print_reverse(a) :
#     print(a[::-1])
#
# print_reverse("python")

# #222
# def print_score(list):
#     print(sum(list)/len(list))
#
# print_score([1,2,3])

# #223
# def print_even(list):
#     for i in list:
#         if i%2 == 0:
#             print(i)
# print_even([1, 3, 2, 10, 12, 11, 15])

# #224
# def print_keys(dict):
#     for i in dict.keys():
#         print(i)
#
# print_keys({"이름":"김말똥", "나이":30, "성별":0})


#225
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
#
# def print_value_by_key(a,b):
#     print(a[b])
# #
# # print_value_by_key(my_dict,"10/26" )
#
# #226
# def print_5xn(string):
#     print(string[0:5])
#     print(string[:-1])

# print_5xn("아이엠어보이유알어걸")

#227
def printmxn(string, a):
    min = int(len(string)/a)
    for x in range(min):
        print(string[:])

# 버블정렬, 카운트정렬, 선택정렬, 델타, 부분집합, 이진검색, 풍선팡2, 사다리