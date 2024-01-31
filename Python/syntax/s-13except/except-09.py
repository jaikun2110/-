"""

사용자 지정 예외객체 만들기

"""
class BirdException(Exception):
    pass

#%%

def HiBird(hi):
    if hi=='dead':
     raise BirdException("새가죽음")
    print("반갑습니다")
    
    
#%%
HiBird('Hello')

HiBird('dead')

#%%
try:
    HiBird('dead')
except BirdException as e:
    print("[Birdexception]",e)