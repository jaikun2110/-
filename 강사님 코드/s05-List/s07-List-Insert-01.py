# 리스트에 요소 삽입 : insert()
# 리스트의 특정 위치에 요소를 삽입
# 해당하는 위치의 요소부터 마지막 요소는 뒤로 밀림
# insert(위치, 값)

lst = ['하나', '둘']

lst.insert(1, '삽입')
print(lst)

# 맨 앞에 삽입
lst.insert(0, '영')
print(lst)

lst.insert(len(lst) * -1, '영영')
print(lst)


# 맨 마지막 삽입 : append()와 같은
lst.insert(len(lst), '끝')
print(lst)

# [주의]
# 원래의 맨 마지막 요소는 뒤로 한 칸 이동
lst.insert(-1, '마지막')
print(lst)
