# Dict
# 딕셔너리의 튜플(키, 값) 목록 추출


# 기본형
dt = {
    "title": "진달래 꽃",
    "author": "김소월",
    "content": "나 보기가 역겨워 가실 때에는..."
}

#%%
# 딕셔너리의 튜플(키,값) 목록 추출
items = dt.items()
print(type(items), items) # <class 'dict_items'>

#%%

items = list(dt.items())

key, value = items[0]
print('key:', key)
print('value:', value)

#%%

# items -> tuple
# items = tuple(dt.items())

#%%
# items -> list
items = list(dt.items())
print(type(items)) # <class 'list'>

# 각 리스트는 튜플로 구성
title = items[0]
author = items[1]
content = items[2]

print(type(title), title)
print(type(author), author)
print(type(content), content)

