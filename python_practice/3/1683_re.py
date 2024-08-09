number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    increase_user()
    user_info = {}
    user_info['name'] = name       
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다!')
    return user_info


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

result = list(map(create_user, name, age, address))
print(result)





# li = []                             # 생성자 정보를 저장하는 리스트
# for i in range(5):                  # for루프를 통해 5명의 사용자를 만듬
#     A = create_user(name[i], age[i], address[i])    # 함수의 반환값을 프린트 하려면 변수에 할당해야댐
#     li.append(A)

'''
예를 들어, 첫 번째 반복(i=0)에서는 create_user('김시습', 20, '서울')이 호출됩니다. 
이 함수는 {'name': '김시습', 'age': 20, 'address': '서울'}라는 딕셔너리를 반환하고, 
이 딕셔너리가 A에 저장됩니다.

li.append(A)
목적: 앞서 생성된 사용자 정보를 리스트 li에 추가합니다.
역할: append 메소드는 리스트 li의 끝에 새로운 요소(A)를 추가합니다. 
이로써, 각 반복이 끝날 때마다 li 리스트에는 새로운 사용자 정보가 누적됩니다.

예를 들어, 첫 번째 반복 후 li 리스트는 다음과 같이 업데이트됩니다:
li = [{'name': '김시습', 'age': 20, 'address': '서울'}]
두 번째 반복 후 li 리스트는 다음과 같이 업데이트됩니다:
li = [{'name': '김시습', 'age': 20, 'address': '서울'}, 
      {'name': '허균', 'age': 16, 'address': '강릉'}]
이 과정이 다섯 번 반복되면 li 리스트는 다섯 명의 사용자 정보로 채워집니다.
이렇게 생성된 li 리스트는 이후 다른 작업(예: 데이터베이스 저장, 화면 출력 등)에서 사용할 수 있습니다. 
각 사용자 정보는 딕셔너리 형태로 저장되어 있으며, li는 이러한 딕셔너리들의 리스트입니다

'''



# print(li)


