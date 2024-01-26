
"""
for 변수 in 리스트
for 변수 in 튜플
for 변수 in 문자열
모두 사용 가능



"""

ls = [1,3,5,6,7]
for l in ls:
    print(l)
    
    
#%%

for ch in 'abcef':
 print(ch)
 
#%%

"""
구구단 
2단부터 9단까지

"""

x=0
a=2
b=3
c=4
for n in range(3):
 for x in range(1,10):
    
    xa=x*a
    xb=x*b
    xc=x*c
    print(a,"*",x,"=",xa,"   ",b,"*",x,"=",xb,"   ",c,"*",x,"=",xc)
    if x==9 :
        a+=3
        b+=3
        c+=3
        
    













