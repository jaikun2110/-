"""
문자열 삽입
결과=삽입할 문자열.join(원본 문자열)
원본 문자열의 각 문자들 사이에 문자열을 삽입


"""

s="abcdef"
t=','.join(s)

print(t)

#리스트

nu=['010','1234','4567']

cs ='-' .join(nu)

print(cs)

#%%
"""
문자열 분할: split()
문자열을 분할아여 리스트로 생성

"""
hp=cs.split('-')
print(hp)

print(f"{hp[0]}-{hp[1]}-{hp[2]}")
print("{0}-{1}-{2}".format(hp[0], hp[1],hp[2]))