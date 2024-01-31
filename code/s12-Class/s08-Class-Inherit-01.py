# -*- coding: utf-8 -*-

# 상속
"""
class 클래스이름(부모클래스):
   ... 
"""

#%%
# 부모 클래스
class Parent:
    def __init__(self, name, age): # 부모생성자
        self.name = name
        self.age = age
        
    def info(self):
        print(f"name({self.name}), age({self.age})")
        
#%%
p = Parent("부모", 67) 
p.info()       

#%%

# 자식 클래스
class ChildA(Parent):
    def __init__(self, name, age): # 자식 생성자
        Parent.__init__(self, name, age)

#%%

ca = ChildA('홍길동', 34)        
ca.info() # 부모의 메소드가 호출

#%%

# 자식 클래스
class ChildB(Parent):
    def __init__(self, name, age, tel):
        super().__init__(name, age)
        self.tel = tel

    def info(self): # 메소드 오버라이딩(재정의)
        # super().info() # 부모 메소드 호출
        # print("전화번호:", self.tel)
        print(f"name({self.name}), age({self.age}), tel({self.tel})")
        
#%%

cb = ChildB("전우치", 30, "010-1234-5678")        
cb.info() # 자신의 메소드가 호출


#%%

# 다중상속
class ChildX(ChildA, ChildB):
    def __init__(self, name, age, tel):
        ChildB.__init__(self, name, age, tel)
        

cx = ChildX("임꺽정", 45, "010-0007-0007")        
cx.info()

#%%

# 다중상속
class ChildY(ChildA, ChildB):
    def __init__(self, name, age):
        ChildA.__init__(self, name, age)
        
    def info(self):
        ChildA.info(self)            

cy = ChildY("와이맨", 55)        
cy.info()
