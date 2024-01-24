"""
리스트에 요소 추가: append()
기존의 리스트에 새로운 요소 추가
기존 요소의 마지막에 추가됨


"""
lst=[]

lst.append(8)
lst.append(9)
lst.append(10)

print(lst)

lst.append([7,6,5])
#리스트를 추가할시 하나의 리스트로서 추가됨

print(lst)
print(len(lst))


lst.append(1)

print(lst)

#%%

"""
리스트 요소 삽입:intsert()
리스트의 특정위치에 요소를 삽입함
insert(위치,값)

"""


lst=['하나','둘']

lst.insert(1, '중간')

print(lst)

lst.insert(0, '처음')# = lst.insert(len(lst) * -1, '처음')

print(lst)

lst.insert(len(lst), '마지막')# = lst.insert(-1, '마지막')


print(lst)

#%%


""" 
리스트 정해진 요소 삭제:remove()
리스트.remove(값)

"""


lst=['사과', '바나나', '사과', '오렌지']

lst.remove('사과')

print(lst)#같은 요소가 여러개여도 처음찾은 요소만 삭제됨

ls=['사과', '바나나', '사과', '오렌지']

ap=ls.index('사과')#인덱스를 찾아 삭제
del ls[ap]
print(ls)


hd = lst.index('hd')#인덱스 추출시 존재하지않으면 에러로 종료됨

print(hd)
