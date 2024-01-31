"""
사칙연산을 수행할 수 있는 클래스를 생성할것

총합과 평균 또한 구할것


"""
a=int(input("숫자1 "))
b=int(input("숫자2 "))

class Cul:
    def __init__(self):
        self.total = 0
        
    def ad(self,nu1,nu2):
        self.t=nu1+nu2
        return self.t
    def mi(self,nu1,nu2):
        self.t=nu1-nu2
        return self.t
    def mul(self,nu1,nu2):
        self.t=nu1*nu2
        return self.t
    def di(self,nu1,nu2):
        self.t=nu1/nu2
        return self.t
    
comp
    
        
c1=Cul()
t1=c1.ad(a,b)
t2=c1.mi(a,b)
t3=c1.mul(a,b)
t4=c1.di(a,b)
print("두숫자를 더한 값",t1)
print("두숫자를 뺀 값",t2)
print("두숫자를 곱한 값",t3)
print("두숫자를 나눈 값",t4)

#%%
b=list()


class Lst:
    def to(self,ls):
        self.t=sum(ls)
        return self.t
    def ave(self,ls):
        if sum(ls)>0:
            self.a=sum(ls)/len(ls)
        return self.a
    
    
cla=Lst()


while len(b)<10:
    a=int(input("숫자1 "))
    b.append(a)
    c1=cla.to(b)
    c2=cla.ave(b)
    print("총합은",c1,"평균은",c2)
    