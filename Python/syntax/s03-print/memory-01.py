"""파이썬에서 변수와 메모리
id(variable):식별자
객체를 식별할수있는 고유의 번호
메모리 연계
id가 같으면 동일한 메모리를 참조함

"""


helo="helo"
world="helo"

print(id(helo), id(world))#동일한 값이므로 동일한 메모리

