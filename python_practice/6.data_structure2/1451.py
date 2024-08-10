# 아래 함수를 수정하시오.
def difference_sets(set_A, set_B):
    return set_A.difference(set_B)


result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)
