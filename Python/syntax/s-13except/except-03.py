"""
변수=eval("문자열")
문자열이 코드라고 가정하고 평가해서 실행하는것
ex) x=("10**3")
권장하지 않ㅇ므
"""

try:
    x=10***3#문법오류는 예외처리하기 어려움
    
    print(x)
except SyntaxError as e:
    print("문법오류")
    
print("종료")
    