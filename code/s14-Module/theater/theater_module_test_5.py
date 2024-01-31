# -*- coding: utf-8 -*-

# 모듈이름을 프로그램에서 다른 이름으로 바꿔 사용
# import 모듈이름 as 별칭
# 별칭.함수()
# 별칭.변수
# 
# from 모듈명 import 기능(또는 함수)

# import theater_module as tm
# from theater_module import *

# 지정된 모듈에 있는 일부 기능을 임포트(import)
# import에 지정된 기능만 사용 가능
# 사용할 때 기능(함수) 이름을 별칭으로 사용(추천하지 않음)
from theater_module import price as pr
from theater_module import price_morning as pm
from theater_module import price_soldier as ps

print("# theater_module_test")

pr(5)    
pm(3)
ps(2)

#%%

from theater_module import ADULT_PRICE, MORNING_PRICE, SOLDIER_PRICE

print("성인:", ADULT_PRICE)
print("조조:", MORNING_PRICE)
print("군인:", SOLDIER_PRICE)
