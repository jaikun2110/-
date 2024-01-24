""" 
부분집합
a.issubset(b)

a는 b의 부분집합인가

결과:True,False
"""


a={'A','B','C','D','E'}
b={'C','D','E','F','G'}

c={'E','F','G'}

sab=a.issubset(b)
sbc=c.issubset(b)

print(sab,sbc)