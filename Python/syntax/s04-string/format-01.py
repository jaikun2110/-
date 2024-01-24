"""
문자열 포맷팅
문자열 포맷코드 
%s :문자열
%c:문자
%d:정수
%f:실수
%o:8진수
%x:16진수


"""

n=99
print("이숫자는 정수 %d 임" %n)
print(f"이숫자는 정수 {n} 임" )
print("이숫자는 정수 {0} 임" .format(n))

#%%

na="길동"
ag=30
us="이름은 %s 나이는 %d 이다" %(na,ag)

print(us)


#%%


"""
문자(charactor) : 하나의 문자
예시) a, A, 1, 한글, #, X 모두 문자로 사용가능
문자열 과는 다른데 문자열은 주로 작은 따옴표를씀
문자형 포맷(%c)에 문자열 지정시 오류
"""

ch='A'
print("문자 포맷 : (%c)" %ch)

asn = 65 #ASCII 코드 65 는 'A'임

print("문자 아스키코드 : (%c)(%d)" %(asn, asn))

asb = asn+1 #66 = 'B'

print("문자 아스키코드 : (%c)(%d)" %(asb, asb))

hexa=0x41
print(print("문자 아스키코드 : (%c)(%d)(0x%x)(0o%o))" %(hexa,hexa,hexa,hexa)))



#%%



sv = 50

print("오늘 눈이 올 확률 : (%d)%%" %sv) #%를 두번 입력하면 '%'가 출력 됨