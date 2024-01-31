# 리스트에서 모든 요소를 제거 : clear()
# 리스트.clear()

#%%
lst = ['삼성', 'LG', 'SK', 'HD', 'HD']

print(id(lst), lst)

#%%

# clear()
lst.clear()
print(id(lst), lst)

#%%

# 리스트에 빈 리스트 할당을 해서
# 모든 요소를 지우는 효과냄
# clear()와는 차이가 있다.
lst = []
print(id(lst), lst)
