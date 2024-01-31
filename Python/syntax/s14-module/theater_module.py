
"""
모듈
서로 관련이 있거나 비슷한 기능을 하는
함수 또는 클래스등

모듈화
개발을 용이하게 하기위해 프로그램의 기능을
독립적인 작은 단위로 나누ㅡㅁ


import
하나의 파이썬(*.py)파일(모듈)
파일을 사용하기위해 로딩

"""
#theater_module.py


#변수
ADULT_PRICE=10000
MORNING_PRICE=6000
SOLDIER_PRICE=4000

def price(people):
    print("{0}명 가격은 {1}".format(people, people*10000))
    
def price_morning(people):
    print("{0}명 조조가격은 {1}".format(people, people*6000))

def price_soldier(people):
    print("{0}명 군인가격은 {1}".format(people, people*4000))
    
    
    
#%%
"""
모듈을 다른파일에서 로딩할때 실행되지 않도록 처리
시스템변수:__name__이 가지고 있는 값 이용

"""
print("module",__name__)
if __name__ == "__main__":    
    price(5)
    price_morning(3)
    price_soldier(2)