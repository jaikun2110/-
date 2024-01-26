# 리스트 삭제
# del 명령어
# del list[index]
# del list[start:end]

lst = [1,2,3,4,5]
print(id(lst))

del lst[2]

# 2번째 요소인 3의 값이 삭제
print(lst) # [1, 2, 4, 5]

# 슬라이싱을 하여 삭제 가능
del lst[1:3]
print(lst) # [1, 5]

# 전체를 삭제
# id의 변화는 없다(메모리의 변동은 없다)
del lst[:]
print(lst, id(lst)) # []
