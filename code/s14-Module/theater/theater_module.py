# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:04:59 2024

@author: Solero
"""

# theater_module.py

# 변수
ADULT_PRICE = 10000  # 성인
MORNING_PRICE = 6000 # 조조
SOLDIER_PRICE = 4000 # 군인

# 일반가격
def price(people):
    print("{0}명, 영화표 가격은 {1}원입니다.".format(people, people * 10000))

# 조조 할인 가격    
def price_morning(people):
    print("{0}명, 조조 할인 영화표 가격은 {1}원입니다.".format(people, people * 6000))    

# 군인 할인 가격    
def price_soldier(people):
    print("{0}명, 군인 할인 영화표 가격은 {1}원입니다.".format(people, people * 4000))    
    
    
#%%
# 모듈을 다른 파일에서 로딩할 때 실행되지 않도록 처리
# 시스템변수 : __name__ 이 가지고 있는 값을 이용
print("[theater_module.py] ", __name__)
if __name__ == "__main__":
    price(5)    
    price_morning(3)
    price_soldier(2)