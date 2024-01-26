# print(인자, end='\n')
# 옵션: end, 디폴트값은 end='\n'
# 전체 인자의 내용을 출력후에 맨마직에 새로운 라인으로 이동
# Line Feed : 라인을 다음 라인으로 이동(Enter)
# ASCII: 0x0D(13), 0x0A(10)
# Windows : CRLF(\r\n)
# Unix, Linux : LF(\n)
# MacOS : CR(\r)
# 
# CR(Carriage Return) : 현재 커서에서 맨 앞으로 이동하는 동작 
# LF(Line Feed) :  커서는 그대로 있고, 줄만 바꾸는 동작
# CRLF : 두 가지 개행문자를 모두 수행

#%%
print("안녕", end='')
print("하세요")

#%%

t1 = '010'
t2 = '1234'
t3 = '5678'

print(t1, t2, t3, sep='-')

print(t1, end='-')
print(t2, end='-')
print(t3)

#%%


