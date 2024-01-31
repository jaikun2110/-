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

# dict.items()

for item in contents.items():
    # print(item)
    print('key:', item[0])
    print('val:', item[1])
    
#%%

for item in contents.items():
    key, val = item # unpack tuple 
    print('key:', key)
    print('val:', val)
    
#%%

# unpacking해서 키, 값을 변수에 받음
for key, val in contents.items():
    print(f'{key} : {val}')
    
#%%

# 키목록을 얻어서 키에 해당하는 값을 찾음
key = '4층'
print(f'{key} : ', contents[key])
print(f'{key} : ', contents['4층'])

#%%
for key in contents.keys():
    print(f'{key} : ', contents[key])
    
#%%

lst = [('1층','전시장'), 
       ('2층','매장'), 
       ('3층','사무실'), 
       ('4층','통제실')]    

for item in lst:
    print(item, ':', item[0], item[1])    

for k, v in lst:
    print(k, ':', v)    
    