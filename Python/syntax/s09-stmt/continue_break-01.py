
"""
반복문 흐름제어
continue
break

break:for반복문 탈출
"""
for n in range(8):
    print(n)
    if n>4:
     break
 
#%%

"""
continue
다음 명령문을 실행하지 않고 넘어감

"""

for n in range(20):
    if n<11:
     print(n)
     continue
    elif n<=8:
     print("계속")
    else:
     break