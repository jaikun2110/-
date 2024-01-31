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

# 찾기: 키가 존재하지 않으면?
# 예외발생: KeyError: 'age'
# age = poetry['age']
# print(f"시인 {poetry['author']}의 나이는 {age}이다.")

#%%

# 딕셔너리.get(키)을 사용하면 키가 존재하지 않아도
# 프로그램이 종료되지 않고 None 값을 리턴한다.
age = poetry.get('age')
print(f"시인 {poetry['author']}의 나이는 {age}이다.")

#%%

# 키를 찾지 못하면 기본값을 지정
# 키를 찾지 못하면 기본값을 리턴
agx = '모름'
age = poetry.get('age', agx)
author = poetry['author']
print(f"시인 {poetry['author']}의 나이는 {age}니다.")

