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
