# 아래 함수를 수정하시오.
def add_item_to_dict(dict, key, value):
    dict.update({key:value})
    return dict
    

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
