"""
문자열 함수
문자갯수 확인:count()

"""
s ="hobby"

print("count = ", s.count("b"))#s변수 안에 b가 몇개인가

print("'hello'.count(l):","hello".count('l'))

b="wellcome to korea"

sp =  b.count(' ')

print(f"'{b}'.count(' '):{sp}" )

#%%

tel = "010-1234-5678"
tc=tel.count('-')
print(f"'(tel)'.count('-') : {tc}")

#%%

str="hello,my,name"

ac = str.count('abc')
print(f"'{str}'.count('abc') : {ac}")