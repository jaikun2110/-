# 문자열 함수 : find()
# 처음 만나는 문자열을 찾음
# 결과 : 문자열의 위치, -1(찾지 못하면)

r = "0123456789012345678901234567890"
s = "Python is the best choice."
ipos = s.find('i')
kpos = s.find('k')

print(r)
print(s)
print(f"'{s}'.find('i') : ", ipos) # 7
print(f"'{s}'.find('k') : ", kpos) # -1

#%%

print(f"'{s}'.find('is') : ", s.find('is'))   # 7
print(f"'{s}'.find('the') : ", s.find('the')) # 10

#%%

# [문제]
# 문자열을 연속해서 어떻게 찾을 수 있는가?
# 문자열 변수(s)에서 지정된 문자열을 찾아라.
r = "0123456789012345678901234567890"
s = "Python is the best choice."
findstr = 't'

print(r)
print(r)

print(f"문자열 ('{s}')에서 문자열('{findstr}')의 갯수는?", s.count(findstr))
t1 = s.find(findstr)
t2 = s[t1+1:].find(findstr) + t1 + 1
t3 = s[t2+1:].find(findstr) + t2 + 1
print(t1,t2,t3) # 2 10 17

#%%

t1 = s.find(findstr)
s1 = s[t1+1:]  # 슬라이싱
t2 = s1.find(findstr) + t1 + 1
s2 = s[t2+1:]  # 슬라이싱 
t3 = s2.find(findstr) + t2 + 1
print(t1,t2,t3) # 2 10 17

#%%

# 결과 = 문자열.find(찾을 문자열, 시작위치)

t1 = s.find(findstr)
t2 = s.find(findstr, t1 + 1)
t3 = s.find(findstr, t2 + 1)
print(t1,t2,t3) # 2 10 17
