
"""
while문을 이용해
1부터 100까지 1씩 증가시켜
3의 배수와 5의 배수를 각각 출력하라

"""

a=0
b=0
l3=[]
l5=[]
while a<=100:
    a+=1
    b+=1
    if b % 3==0:
        l3.append(b)
    elif b % 5==0:
        l5.append(b)
print(l3)
print(l5)
