# print() 함수
# 문자열포맷.format(value, value)
#

msgfmt = "{0}, {1}!!!"

hello = "Hello"
world = "World"

print("{0}, {1}!!!".format(hello, world))
print(msgfmt.format(hello, world))
print(msgfmt.format('안녕하세요', '환영합니다.'))

#%%

helloworld = msgfmt.format(hello, world)
print(helloworld)

#%%

a = 10
b = 20
c = a + b
numfmt1 = "더하기: {0} + {1} -> {2}"
numfmt2 = "더하기: {2} <- {0} + {1}"
print(numfmt1.format(a, b, c))
print(numfmt2.format(a, b, c))



