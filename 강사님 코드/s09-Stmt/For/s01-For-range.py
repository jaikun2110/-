# -*- coding: utf-8 -*-

# 반복문 : for
# range(n)
# n : 0 ~ n-1

n = 10
for x in range(n): # 10번 반복: 0부터 9까지
    print(x)

#%%

# 1부터 10까지 합을 구하라.

t = 0
for x in range(10): # x: 0,1,2, ... 9
    t = t + x + 1
    print(f"x({x}), t({t})")
    
print(f"최종결과: ({t})")
    