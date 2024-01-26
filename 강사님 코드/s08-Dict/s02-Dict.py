# Dict
# 키참조 : dict[키]

# 기본형
poetry = {
    "title": "진달래 꽃",
    "author": "김소월",
    "content": "나 보기가 역겨워 가실 때에는..."
}

print(poetry)

#%%

# 찾기:
# 키참조: 키를 통해서 값을 참조
title = poetry['title']
author = poetry['author']
content = poetry['content']

print(title)
print(author)
print(content)

#%%

# 추가:
# 새로운 키(없는 키)로 값을 지정하면 추가(등록)
poetry['age'] = 34
print(poetry)

#%%

# 변경:
# 키가 존재하면 지정된 값으로 변경(수정)
# 키에 해당하는 값는 수정
poetry['age'] = 36
print(poetry)

#%%    

# 삭제: 
# 키에 해당하는 요소를 찾아서 키와 값을 모두 삭제    
# del 딕셔너리['키']
del poetry['age']
print(poetry)

#%%

# 삭제: 없는 키를 삭제하려 하면?
# 예외발생: KeyError: 'tel'
del poetry['tel']



    
