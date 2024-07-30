'''
Q. 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

예) 생성된 비밀번호 : nav51!
'''



secret = "http://naver.com"
my_str = secret.replace("http://", "")
my_str1 = my_str.replace(".com", "")
my_str2 = my_str1[:2] + len(my_str1) + my_str1.count(e) + "!"
print(my_str2)
# del secret[-4:]
# secret_number = "secret" + "len(secret)" + "secret.count[e]"

# print(f"http://naver.com의 비밀번호는 {secret_number} 입니다.")

# url = "http://naver.com"
# my_str = url.replace("http://", "") # 규칙 1
# my_str = my_str[:my_str.index(".")]
