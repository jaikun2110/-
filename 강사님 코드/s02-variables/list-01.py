# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:04:28 2024

@author: YONSAI
"""

# 리스트 요소 삭제 : remove()
# list.remove(value)
# 처음 찾은 값에 해당하는 요소를 삭제

lst = ['삼성', 'SK', 'LG', 'APPLE', 'LG']

lst.remove('LG')

print(lst) # ['삼성', 'SK', 'APPLE', 'LG']

#%%
# 해당하는 값을 찾아서 인덱스로 삭제하려면?
sk = lst.index('SK')
del lst[sk]
print(lst)

#%%

# 값으로 찾아서 리스트 요소의 위치를 리턴
# 값에 해당하는 요소를 찾지 못하면 종료
# list.index(value)

# ValueError: 'HD' is not in list
# 프로그램 종료
hd = lst.index('HD')
print('HD:', hd)
#%%

"""
append() : 요소를 한 자리에 추가시켜줌

extend() : append() 여러 개를 동시에 처리한다고보면됨

. => 접근 제한자, 객체 내부의 요소에 접근할 수 있게 해주는 요소
:: => 이것도 접근 제한자, 다만 이건 생성 안 된 요소에 접근, 파이선은 안씀

"""
a =[]
b =[3,5,1]
c= ["a","b"]
d= ["c","d"]
g= b.sort()

a.append(c)
b.extend(c)
print (a,b)
print (g,b)


#%%

s= True

s2 = 1 + s 

print(s2, type(s))






s = 1 + True * bool("") #2 falsy한 값들
print(s)


"""
c언어에서는 boolean이 없음

다 0,1

boolean의 지원 이유: 타입간의 구분을 명확히 하기 위해


"""

print(input("sss ::"))


#%%

a= {1,2,3,4,5}
b={1,2,3,6,7,8}

print((a-b)|(b-a))
print((a|b)-(a&b))