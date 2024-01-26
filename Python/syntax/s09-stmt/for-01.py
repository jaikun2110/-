"""
반복문:for

range(n)

n:0~n-1



"""

n=10
for x in range(n):#10번 반복함
    print(x)
    
#%%

#1부터 10까지 합 구하기
t=0
for x in range(10):
    t+=x+1
    print(f"{x},{t}")
    
#%%
s=1
e=10+1
t=0
for x in range(s,e):#x값은 s부터 e-1값 까지 증가함
    t+=x
    print(f"{x},{t}")
#%%    
"""

문제

for range를 이용하여
다음의 합을 구하라
1부터 10까지 연속된 숫자를 생성하여
홀수의 합과 짝수의 합을 구하라
"""
h=0
j=0
x=0
for x in range(11):
    
 if x % 2==0 :#for 문 안의 if문은 띄어써야함
    j+=x
    
 else:
    h+=x
print(j,h)
