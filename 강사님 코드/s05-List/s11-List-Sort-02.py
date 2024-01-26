# 리스트 정렬(sort) : sort()
# 오름차순(ascending) :  작은값 -> 큰값
# 내리차순(descending) : 큰값 -> 작은값
# None = 리스트.sort() 
# 기본 : 오름차순
# 리턴 : None
# 원본이 변경, 요소의 위치가 바뀐다.

score = ['own', 'one', 'two', 'three', 'Three', 'Four']

#%%
# 오름차순
score.sort() 
print(score)
# ['Four', 'Three', 'one', 'own', 'three', 'two']

#%%

score += ['한글', '시작']
print(score)

score.sort()
print(score)
