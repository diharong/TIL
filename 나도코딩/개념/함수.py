def open_account():
    print("새로운 계좌가 생성되었습니다.")
# 함수는 정의만 되는 것이지 실제로 호출을 하기 전까지는 실행되지 않음!!

open_account() # 함수 호출

def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

balance = 0 #잔액
balance = deposit()
print(balance)
