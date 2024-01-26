# 리스트에 요소 추가 : append()
# 기존의 리스트에 새로운 요소를 추가
# 기존의 요소의 끝에 추가

lst = []

lst.append(10)
lst.append(9)
lst.append(8)

print(lst)

# 리스트 더하기와 차이는?
# 새로 더해지는 리스트를 하나의 요소로 처리리
lst.append([7,6,5])

print(lst) # [10, 9, 8, [7, 6, 5]]

lst.append(0)
print(lst) # [10, 9, 8, [7, 6, 5], 0]
print(len(lst)) # 5

# 여러개의 요소를 나열식으로 추가할 수 있는가?
# 오류 : 한 개의 요소가 추가 가능
# lst.append(1,3,5)


