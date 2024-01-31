# 파이썬에서 변수와 메모리
# id(variable) : 식별자
# 객체를 식별할 수 있는 고유의 번호
# 메모리 연계 : 메모리 주소와 맵핑된 형태
# id가 같으면 동일한 메모리를 참조하고 있다.

hello = "Hello"
world = "Hello"
print(id(hello), id(world))

#%%
num1 = 100
num2 = 100
print('num1:', id(num1), num1)
print('num2:', id(num2), num2)

num2 += 1
print('num1:', id(num1), num1)
print('num2:', id(num2), num2)

print(num1, num2)

num2 += 1
print('num2:', id(num2), num2)

num2 = "안녕"
print('num2:', id(num2), num2, type(num2))

