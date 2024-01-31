# Dict
# 딕셔너리의 키, 값 목록 추출


# 기본형
dt = {
    "title": "진달래 꽃",
    "author": "김소월",
    "content": "나 보기가 역겨워 가실 때에는..."
}

#%%

# 딕셔너리의 값 목록 추출

values = dt.values()
print(type(values), values) # <class 'dict_values'> 

#%%

values = list(dt.values())
print(values[0])
print(values[1])
print(values[2])
