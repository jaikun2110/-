

import theater_module as tm#theater_module 를 tm으로 사용한다는 함수

#from theater_module import * 모든 기능을 가져옴
#from 모듈 에서 import 부분 만큼 기능을 가져옴

print("module_test")
print("성인",tm.ADULT_PRICE)
print("아침",tm.MORNING_PRICE)
print("군인",tm.SOLDIER_PRICE)


tm.price(5)
tm.price_morning(3)
tm.price_soldier(2)