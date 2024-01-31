# -*- coding: utf-8 -*-

# 예외처리
# 사용자 예외 객체 만들기

# Exception : 예외처리의 기반 클래스
# Exception 클래스를 상속하여 새로운 예외 클래스를 정의할 수 있다.

# BirdException 클래스 정의
class BirdException(Exception):
    pass

#%%
def HiBird(hi):
    if hi == 'dead':
        raise BirdException("새가 죽었습니다.")
    print("안녕? 반갑습니다.")

#%%
HiBird('Hello')    
HiBird('dead') # BirdException: 새가 죽었습니다.

#%%
try:
    HiBird('dead') 
except BirdException as e:
    print("[BirdException] ", e)
    
