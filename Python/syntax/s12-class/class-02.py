
"""
전역변수로 total을 사용하게 되면 모든 cul객체에서
공유함으로 total값이ㅣ 누ㅜ적되어 
각객체별로 값을 처리할수없음
"""
class Cul:
    def __init__(self):#생성자
        print(id(self))
        self.total = 0#속성:메소드
        
    def ad(self,nu):
        self.total += nu
        return self.total
    

#%%
c1=Cul()#객체생성
t1=c1.ad(10)#함수호출

print(t1)
c2=Cul()
t2=c2.ad(5)
print(t2)


#%%

t1=c1.ad(20)
t2=c2.ad(7)
print(t1)
print(t2)