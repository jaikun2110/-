""" 0x = 16진수 0o = 8진수
0o377 = 0xff = 255"""

a=255
b=0o377
c=0xff

print(a==b==c)

#%%
""" 연산자
사칙연산: +, -, *, /
정수 나누기://
나머지 구하기:%, dvmod(x, y)
지수:**
"""
a=10
b=3
c=20

print('a%b=', a%b)
print('c^b=', c**b)

r = a/b#실수 나눗셈
n = a//b#정수 나눗셈

print(r,'\n' , n)

#%%
""" 나머지:%
몫과 나머지 divmod(x,y) 데이터타입(tuple)
"""
g=divmod(a,b)
print('10을 3으로 나눈 몫과 나머지는', g)

gm, gn=g#몫과 나머지 나누기

print('10을 3으로 나눈 몫',gm, '나머지', gn)



#%%

w1 = a//b#a를 b로 나눈 몫
w2 = a - w1 * b#a를 b로 나눈 나머지

print('10을 3으로 나눈 몫',w1, '나머지', w2)



