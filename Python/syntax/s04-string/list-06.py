"""
리스트 삭제
del 명령어
del list[index]
del list[start:end]

"""

lst = [1,2,3,4,5]

del lst[2]#리스트의 3번째 요소 삭제

print(lst)

del lst[1:3]#슬라이싱하여 삭제

print(lst)

del lst[:]#전체삭제

print(lst)

#%%

"""
id가 바뀜(새로운 메모리에 할당)

리스트 삭제시 적은 메모리 소모함

"""
print(lst,id(lst))