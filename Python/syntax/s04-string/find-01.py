"""
문자열 함수
find()
처음만나는 문자열을 찾음
결과:문자열의 위치,-1

"""

sen = "python is best best"

ip = sen.find('i')
kp = sen.find('k')

print(ip)

print(f"'{sen}'.find(i): ", ip)

print(f"'{sen}'.find(is): ", sen.find('is'))


# %%

"""
문자열을 연속해서 찾아라

"""

fs = sen.find('t')

print(fs)
