
"""
함수:람다(lambda)
inline 함수, 익명함수
함수형 프로그래밍

정의와 선언이 동시에 이루어짐
정의선언:함수변수=lambda 파라미터:표현식
"""

def add(a,b):
    return a + b

c=add(10,20)
print("일반함수",c)

#%%

la=lambda a, b:a+b
d=la(10,20)
print(d)


#%%
#1회성 처리함수

print((lambda a,b:a*b)(10,20))

#%%

def ca(what,func,*vals):
    print(what,func(*vals))
    
    
def ad(*vals):
    re = 0
    for va in vals:
        re += va
    return re

ca("더하기",ad, 1,3,5,7,9)

#%%

