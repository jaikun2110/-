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

# 전역변수(total)를 사용하면 모든 Calc 객체에서 
# 공유함으로 total 값이 모두 누적되어
# 각 객체별로 값을 처리할 수 없다.

# 전역변수
total = 0

# 전자계산기: Calc
class Calc:
    def __init__(self): # 생성자
        print(f"[생성자] self({id(self)})")
        # self.total = 0  # 속성: 속성을 생성해서 0을 할당
        
    def add(self, num): # 메소드: 더하기
        global total
        total += num
        return total
        # self.total += num # self.total = self.total + num
        # return self.total
    

#%%

# 클래스에 소속된 함수(메소드)는 외부에서 독립적으로 호출할 수 없다.
# NameError: name 'add' is not defined
# print(add(10))

#%%

c1 = Calc()     # 객체생성: 객체이름(c1)
print("c1:id=", id(c1))
t1 = c1.add(10) # 함수호출: add()
print(t1) # 10

c2 = Calc()     # 객체생성: 객체이름(c2)
print("c2:id=", id(c2))
t2 = c2.add(5)  # 함수호출: add()
print(t2) # 5

#%%
t1 = c1.add(20)
t2 = c2.add(7)
print(t1) # 30
print(t2) # 12

