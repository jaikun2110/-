

ms=r"hello \world\ now"#변수 지정시 텍스트 앞에 r 삽입시 백슬래시 무시

print(ms)


""" ms=r"hello \world\ now\" 이와 같이 문자 끝에 백슬래시 삽입시
오류발생 이럴때는 한칸 띄워 해결"""


#%%

"""복합대입연산자
+=
-=
*=
/=:나눠서 대입(실수)
//=:나눠서 대입(정수)
%=:나머지를 대입
**=:거듭제곱을 대입
"""
#%%

a=10
b=20
c=a+b

a+=b
print(a)

a-=b
print(a)

a*=b
print(a)

a/=b
print(a)
