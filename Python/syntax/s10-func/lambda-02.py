def ca(what,func,a,b):
    print(what,func(a,b))
    
    
def ad(a,b):
    
    return a+b

ca("홀수",lambda a,b:a+b,1,3)#람다식
ca("더하기",ad, 1,3)

ca("홀수",lambda a,b:a*b,1,3)
#= def mul(a,b):
#    return a*b  위 람다식과 같음