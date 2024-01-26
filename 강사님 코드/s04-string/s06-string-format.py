# 문자열 포맷팅(String Formatting)
# 문자열 포맷 코드
# %s : 문자열(string)
# %c : 문자(character)
# %d : 정수(10진수, decimal)
# %f : 실수(float)
# %o : 8진수(octal)
# %x : 16진수(hexa-decimal)
# 
# 형식
# 포맷문자열 % 변수
# 포맷문자열 % (변수, ...)

#%%

# 문자(character) : 하나의 문자
# 'a', 'A', '1', '한', '글', '#', "X"

# 포맷(%c)에 문자열을 전달하면 오류
# TypeError: %c requires int or char
# chA = 'ABC'

chA = 'A'
print("문자 포맷 : (%c)" % chA)

# ASCII 코드 : 65('A')
numA = 65
print("문자 포맷 : (%c)(%d)" % (numA, numA))

numB = numA + 1 # 66('B')
print("문자 포맷 : (%c)(%d)" % (numB, numB))

hexA = 0x41
print("문자 포맷 : (%c)(%d)(0x%x)(0o%o)" % (hexA, hexA, hexA, hexA))



