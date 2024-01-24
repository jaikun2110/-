"""
리스트확장:extend()

기존에 있는 리스트에 요소를 추가하여 확장
다수 append()를 하나로 처리하는 효과
추가 리스트는 개별적으로 하나씩 append가 된다


"""

lst =  ['삼성','sk', 'lg']

lst.extend(['apple','hd'])

print(lst)

lst += ['nc','kt']

print(lst)

#%%

elt = ['ab', 'cd']

abc= ['abc'].extend(elt)#리턴값은 없음

print(abc)