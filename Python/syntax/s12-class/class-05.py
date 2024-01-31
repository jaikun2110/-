"""
상속

"""

class Parent:
    def __init__(self,name, age):
        self.name=name
        self.age=age
        
    def info(self):
        print(f"name({self.name}, age({self.age})")
        
        
#%%

p=Parent("\부모", 64)
p.info()

#%%

class ChildA(Parent):
    def __init__(self,name,age):
        Parent.__init__(self,name,age)
        
        
#%%

ca = ChildA("홍길동",34)
ca.info()

#%%
class ChildB(Parent):
    def __init__(self,name,age,tel):
        Parent.__init__(self,name,age)
        self.tel = tel#추가도 가능
        
        
cb = ChildB("길동",30,"010-1234")

cb.info()#자신의 메소드 호출


#%%

class ChildX(ChildA,ChildB):
    def __init__(self,name,age,tel):
        ChildB.__init__(self,name,age,tel)
    
    
cx=ChildX("꺽정",54,"10-0000")
cx.info()

