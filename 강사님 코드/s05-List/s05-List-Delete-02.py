# 리스트 삭제
# del 명령어
# del list[index]
# del list[start:end]

lst = [1,2,3,4,5]
print(id(lst))

# 전체를 삭제 
lst = []

# id가 바뀜(새로운 메모리에 할당)
# 장점: 속도가 빠르다.
print(lst, id(lst)) # []
