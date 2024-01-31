"""
예외처리
잘못된 동작을 했을 때 오류발생의 대응
런타임 오류처리
    1.문법오류는 예외처리를 할 수 없다
    2.파이썬은 인터프리터 방식이기에 
    실행 할 때 문법 오류가 발생할수있다
    구문오류는 예외처리에 해당하지 않음
    3.오류가 발생하면 프로그램이 중단되며 오유메세지 출력
    4.예외처리를 하면 오류를 잡아서 중단없이 실행가능        



"""

x=110
y=0
try:
    z=x/y#예외발생시 다음블록을 실행함 실행문은 실행하지 않음
except ZeroDivisionError as e:#예외처리
    print("예외발생",e)

print("종료")
#z=x/y
#print(z)
if y ==0:
    print("나눌수 없음")
    sys.exit()#종료명령어
    
#%%

na="길동"

try:
    print(na)
    print(ag)
except NameError as e:
    print("예외발생",e)
