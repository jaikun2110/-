

"""

조건식이 만족하는동안 반복
while 조건식:
    명령문
"""

n = 1
t = 0
while n<=10:
    t+=n
    n += 1
    
print(t)

#%%

cn=0
to=0

while True:
    if cn > 100:
        break
    cn += 1
    to+= cn
print(cn,to)