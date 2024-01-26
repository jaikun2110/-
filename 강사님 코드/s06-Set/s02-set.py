# 세트(set) 자료형

#%%

# 순서가 보장되지 않는다.
nums1 = { 1,3,5,55,7,0,1,2,9 }
print(nums1) # {0, 1, 2, 3, 5, 7, 9, 55}

#%%

# 중복을 허용하지 않는다.
nums2 = { 1,2,4,1,2,3,4}
print(nums2) # {1, 2, 3, 4}

#%%

# True는 1로, False는 0로 처리
# True, False, 1, 0
tfset1 = { 0, 1, True, False, 10, '세트'}
print(tfset1) # {0, 1, 10, '세트'}

# 먼저 지정된 값으로 선택
tfset2 = { True, False, 0, 1, 10, '세트'}
print(tfset2) # {False, True, 10, '세트'}

#%%

# 순서를 보장하지 않는다.
weeks = {'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'}
print(weeks) # {'Thu', 'Sun', 'Wed', 'Sat', 'Tue', 'Fri', 'Mon'}

#%%

# True, False를 정수(int) 변환하면 1, 0이 된다.
tn = int(True)
print(tn) # 1

fn = int(False)
print(fn) # 0

#%%

t1 = True
n1 = 10
tn = t1 + n1
print(tn, type(tn)) # 11 <class 'int'>

nt = n1 + t1
print(nt, type(nt)) # 11 <class 'int'>

#%%

tt = 1 + True
print(tt, type(tt)) # 2 <class 'int'>

