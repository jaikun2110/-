
"""
사칙연산을 수행하는 계산기 함수를 각각정의하라

호출하여 실행되는 결과를 출력하라

"""
ls=[]
def pl(a,b):
    c=a+b
    ls.append(c)
    return c
def mi(a,b):
    c=a-b
    ls.append(c)
    return c
def di(a,b):
    c=a//b
    ls.append(c)
    return c
def mu(a,b):
    c=a*b
    ls.append(c)
    return c


a=int(input("숫자? "))
b=int(input("숫자2? "))

print("더한값",pl(a,b))
print("뺀값:",mi(a,b))
print("나눈값:",di(a,b))
print("곱한값:",mu(a,b))





"""
문제1에 정의된 함수를 호출한 
총합,평균을 리턴하는 
함수를 정의하라
총합과 평균을 출력하라
"""


def to(a):
    a=sum(ls)
    return a

def ave(a):
    a=sum(ls)/len(ls)
    return a
to1=to(a)
ave1=ave(a)

print("총합", to1)
print("평균", ave1)



#문제1을 재계산 하는 함수를 정의하고
#처리결과를 예시하라


