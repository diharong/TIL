pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

def create_data(subject, day, title='None'):
    data = {}
    global pro_num
    data['과목'] = subject
    data['일차'] = day
    data['제목'] = title
    data['문제 번호'] = pro_num+1
    pro_num += 1
    return data

result_1 = create_data('python', 3)
result_2 = create_data('web', 1, 'web 연습하기')
result_3 = create_data(*global_data.values())

print(result_1)
print(result_2)
print(result_3)

# print(global_data.items())