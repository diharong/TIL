# 실습 번호.py
number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

number_of_book = 100

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]



def create_user():
    increase_user()
    user_info = {}
    user_info['name'] = name       
    user_info['age'] = age
    print(f'{name}님 환영합니다!')
    return user_info


many_user = list(map(create_user, name, age))


info = list(map(lambda a:{'name':a['name'],'age' : a['age']} , many_user))


def rental_book(info):
    