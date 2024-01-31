# -*- coding: utf-8 -*-

# 반복문 : for

# 딕셔너리 활용
contents = {
    '1층':'전시장',
    '2층':'매장',
    '3층':'사무실',
    '4층':'통제실'
}

#%%
# 키순환 : 딕셔너리에서 요소의 갯수만큼 키만 커냄
for key in contents:
    print(key)

# dict.keys()
for key in contents.keys():
    print(key)    
    
#%%

# 값순환: 딕셔너리에서 요소의 갯수만큼 값만 커냄
# dict.values()
print("# dict.values()")
for value in contents.values():
    print(value)