# Dict
# 딕셔너리의 키, 값 목록 추출


# 기본형
dt = {
    "title": "진달래 꽃",
    "author": "김소월",
    "content": "나 보기가 역겨워 가실 때에는..."
}

#%%

# 키 목록 : dict.keys()
dk = dt.keys()
print('keys:', dk) # dict_keys(['title', 'author', 'content'])

# 키 목록을 튜플로 변환
tk = tuple(dk)
print(type(tk), tk) # <class 'tuple'> ('title', 'author', 'content')

print(f"({tk[0]}) : ", dt[tk[0]]) # title
print(f"({tk[1]}) : ", dt[tk[1]]) # author
print(f"({tk[2]}) : ", dt[tk[2]]) # content

