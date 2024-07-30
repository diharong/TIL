'''
영어 문장이 주어졌을 때 첫 번째 글자는 대문자로, 나머지 글자는 모두 소문자로 변환하는 프로그램을 작성하세요.

# 주어진 문장 : the early bird catches the worm.
The eartly bird catches the worm.
'''

sentence = "the early bird catches the worm."
print(sentence[0].upper() + sentence[1:].lower())
