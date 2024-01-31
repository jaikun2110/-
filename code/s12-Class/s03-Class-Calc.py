# -*- coding: utf-8 -*-

# 클래스: class
# 속성(property): 변수, 클래스에 종속된 멤버변수
# 메소드(method): 함수, 클래스에 종속된 멤버함수
# self: 객체의 식별자
# 생성자: 객체가 생성될 때 호출 됨(옵션), 한 번 자동호출
# 소멸자: 객체가 소멸될 때 호출 됨(옵션), 한 번 자동호출
#         프로그램이 종료될 때 호출 됨
# 정의: 클래스 이름은 첫문자를 대문자로 시작(관례적으로)    
"""    
class 클래스이름:
    def 함수이름(self):
        실행문        
"""  
#%%

# [문제] 사칙연산을 수행하는 계산기를 만들어라.
# 아래의 기능을 수행하는 메소드를 정의하라.
# 더하기, 빼기, 나누기, 곱하기, 총합, 평균

# 전자계산기: Calc
class Calc:
    def __init__(self): # 생성자
        self.total = 0  # 총합
        self.count = 0  # 평균을 구하기 위한 연산 회수
        
    def add(self, num): # 더하기
        self.total += num
        self.count += 1
        return self.total

    def sub(self, num): # 빼기
        self.total -= num
        self.count += 1
        return self.total

    def mul(self, num): # 곱하기
        self.total *= num
        self.count += 1
        return self.total

    def div(self, num): # 나누기
        self.total //= num
        self.count += 1
        return self.total
    
    def tot(self): # 총합
        return self.total

    def avg(self): # 평균
        return self.total / self.count

#%%


