# 문자열 슬라이싱(slicing)
# 특정한 범위를 지정해서 추출
# 추출을 하게되면 기존의 문자열의 변화는 없다.(원본의 변화는 없다)
# 추출된 문자열은 새로운 변수에 할당
#
# 변수 = 문자열[시작번호:종료번호:스텝]
# 시작위치 : 0부터시작
# 종료위치 : 종료번호 - 1까지
# 스텝간격 : 건너뛰기

#%%
# [문제]
# 문자열에 0부터 9까지 지정한 후
# 각각 홀수와 짝수값을 추출하라.

nums = "0123456789"

# 홀수
start = 1       # 시작위치
end = len(nums) # 종료위치
step = 2        # 건너뛰기
odd = nums[start:end:step]
print(f"문자열({nums})에서 홀수는 ({odd})")
print(f"문자열({nums})에서 홀수는 ({nums[1::2]})")

# 짝수
start = 0       # 시작위치
end = len(nums) # 종료위치
step = 2        # 건너뛰기
even = nums[start:end:step]
print(f"문자열({nums})에서 짝수는 ({even})")
print(f"문자열({nums})에서 짝수는 ({nums[::2]})")
