# 리스트(list)
# 여러 형태의 자료들의 연속된 모임
# 변경가능(mutable)

# 리스트 생성
lst0 = [1,3,5,7,9]
lst1 = [2,4,6,8,10]

print(lst0, type(lst0), len(lst0))
print(lst1, type(lst1), len(lst1))

#%%

# 인덱스로 참조
print(lst0[0])  # 첫 번째 요소
print(lst0[-1]) # 마지막 요소
print(lst0[len(lst0)-1]) # 마지막 요소

#%%

# 수정가능
lst1[-1] = 99
print(lst1)

