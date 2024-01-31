# -*- coding: utf-8 -*-

# 반복문 : while
"""
# 조건식이 만족하는 동안 명령문을 실행한다.
# 조건식의 만족 : 참(True)
while 조건식:
    명령문1
    명령문2
    명령문3
"""

#%%

# 무한루프 : 멈추지 않고 반복해서 실행
cnt = 0
tot = 0

while True:
    if cnt >= 100: # 100보다 크거나 같은면 탈출
        break
    
    cnt += 1
    tot += cnt
    print(f"cnt={cnt}, tot={tot}")