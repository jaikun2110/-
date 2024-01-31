# 튜플(Tuple)
# 불변(immutable) 상수 리스트(list)
# 불변 : 요소의 값을 변경할 수 없다.
# 수정(추가, 삭제, 변경)을 할 수 없다.
# 그 외에는 리스트와 비슷하다.
# 장점:
#   - 리스트에 비해서 속도가 빠르다.
#   - 공간절약(메모리)
# 특징:
#   - 딕셔너리(dict) 키로 활용
#   - 함수(function)의 인자로 사용
# 사용:
#   - 요소가 한 개인 경우에는 마지막 요소 뒤에 콤마(,)를 붙여야 한다.     
#   - 튜플변수 = (값, )    
#   - 튜플변수 = (값, 값)    

#%%

jobs = ('요리사', '교사', '사무원')

# 언패킹(unpacking)
chef, teacher, officer = jobs
print("# 언패킹(unpacking)")
print(chef)
print(teacher)
print(officer)

#%%

print("# 인덱스 참조")
print(jobs[0])
print(jobs[1])
print(jobs[2])


#%%

# 언패킹(unpacking)
# 생략: 언더스코어(_)
_, _, off = jobs
print("# 언패킹(unpacking)")
print(off)

cf, _, off = jobs
print("# 언패킹(unpacking)")
print(cf)
print(off)

#%%
# 갯수가 일치하지 않으면 오류

# 원래 튜플의 갯수보다 적은 변수를 지정
# ValueError: too many values to unpack (expected 2)
c, t = jobs

#%%

# 원래 튜플의 갯수보다 많은 변수를 지정
# ValueError: not enough values to unpack (expected 4, got 3)
c, t, o, x = jobs
