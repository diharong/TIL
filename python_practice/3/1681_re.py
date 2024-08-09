number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    increase_user()
    user_info = {}
    user_info['name'] = name        # ['name'] 은 키값 , name 은 매개변수를 통해 벨류값추출
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다!')
    return user_info


print('현재 가입 된 유저 수 :', number_of_people)
A = create_user('홍길동', 30, '서울')
print(A)
print('현재 가입 된 유저 수 :', number_of_people)

'''
create_user('홍길동', 30, '서울')
create_user 함수는 사용자가 전달한 name, age, address를 사전(dict)에 저장한 후, 
이 사전을 반환. 
함수의 반환값을 활용하려면, 호출한 결과를 변수에 저장하거나 즉시 출력해야 함.

'''