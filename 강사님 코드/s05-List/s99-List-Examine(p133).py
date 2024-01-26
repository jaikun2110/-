# 교제 : P133

#%%
# [문제1]
"""
1. 다음 중 리스트의 특징으로 올바른 것은?
    1) 같은 값의 중복을 허용한다.
        lst = [1,2,3,3,3]
    2) 빈 리스트는 생성할 수 없다.
        lst = []
        lst = list()
    3) 숫자면 숫자, 문자면 문자끼리만 넣을 수 있다.
        lst = [1,2,3,'문자',False]
    4) 리스트는 값들을 점으로 구분해 대괄호 안에 넣어 표시한다.
        -> 각 요소는 콤마(,)로 구분한다.

정답: 1번

"""

#%%

# 다음 중 리스트에 해당하는 데이터로 올바른 것은?
# 정답 : 1번(l1)
l1 = [1, 2, 3]       # list
s1 = {1,2,3}         # set
t1 = (1,2,3)         # tuple
d1 = {0:1, 1:2, 1:3} # dict

print(type(l1), l1) # list
print(type(s1), s1) # set
print(type(t1), t1) # tuple
print(type(d1), d1) # dict, {0: 1, 1: 3}

#%%

# 실행 결과를 얻기 위해 '가'에 들어갈 함수로 알맞은 것은?
# 결과 : ['파이썬', '자바', 'C#']
# 정답 : 2번
"""
langs = ["파이썬", "자바"]
langs.가("C#")         
print(langs)
1)add, 2)append, 3)extend, 4)insert
"""
langs = ["파이썬", "자바"]
langs.append("C#")         
print(langs)

# 참고 : append()와 동일한 효과
# insert(index, value)
# langs.insert(len(langs),"C#")         

