# 교제(나도코딩의 파이썬 입문) P141 : 1분 퀴즈
# 딕셔너리 안에 해당하는 키가 존재하는지 
# 검사해서 결과 bool(True, False)로 리턴

nums = {
    "숫자": (1,2,3),
    "홀수": [1,3,5],
    "짝수": {2,4,6}
}

print(nums)

#%%

quest = '짝수'
exist = quest in nums
print(f"'{quest}' in {nums} ->", exist) # True

#%%

quest = '문자'
exist = quest in nums
print(f"'{quest}' in {nums} ->", exist) # False

find = nums.get(quest)
print(f"get({quest}) : {find}, {find != None}") # None, False




