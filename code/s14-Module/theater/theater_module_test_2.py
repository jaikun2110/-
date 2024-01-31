# -*- coding: utf-8 -*-

# 모듈이름을 프로그램에서 다른 이름으로 바꿔 사용
# import 모듈이름 as 별칭
# 별칭.함수()
# 별칭.변수

import theater_module as tm

print("# theater_module_test")
print("성인:", tm.ADULT_PRICE)
print("조조:", tm.MORNING_PRICE)
print("군인:", tm.SOLDIER_PRICE)

tm.price(5)    
tm.price_morning(3)
tm.price_soldier(2)
