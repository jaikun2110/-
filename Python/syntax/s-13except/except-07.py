class Bird:
    def fly(self):
       raise NotImplementedError("예외발생")#예외발생시키기

#%%
"""
예외가 발생되어 프로그램이 종료되므로
다음셀로 이동하여 실행하지 않음
""" 

try:
    
    bird=Bird()
    bird.fly()
except NotImplementedError as e:
    print(e)
#%%


try:
    bird=Bird()
    bird.fly()
except NotImplementedError as e:
    print("기능미구현",e)
    
#%%    
class Eagle(Bird):
    def fly(self):
       print("날다")
       
eagle=Eagle()
eagle.fly
