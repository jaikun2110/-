# 문자열 인덱싱
# 문자열은 연속된 문자들의 집합
# 참조: 특정한 위치의 문자를 본다(읽음)
# 시작위치 : 0부터 시작
# 참조방법 : 문자열[인덱스]
# 참조범위 : 0 ~ n-1, n=len(문자열)
# 제약사항 : 참조는 할 수 있지만 바꿀 수 없다. (read-only)

s ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sl = len(s)  # 문자열의 길이(length)를 리턴
print(sl, ':', s)

#%%
# 참조 : 0부터 25(26-1)
print(s[0], s[1], '...', s[24], s[25])
print(s[0], s[1], '...', s[sl-2], s[sl-1])

#%%

# read-only : 인덱스를 참조해서 값을 바꿀 수 없다.
# TypeError: 'str' object does not support item assignment
# s[0] = 'a'
# s[sl-1] = 'z'

#%%

# 문자열 전체의 값을 변경은 가능
print("바꾸기 전:", s)
s = "abcdefg"
print("바꾸기 후:", s)

#%%



