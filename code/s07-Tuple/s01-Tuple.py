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

# 빈 튜플
t0 = ()
te = tuple()

print(t0, type(t0)) # ()
print(te, type(te)) # ()

#%%

# 요소가 한 개인 경우에는 마지막 요소 뒤에 콤마(,)를 붙여야 한다.
t1 = (99,)
print(t1, type(t1)) # (99,) <class 'tuple'>

#%%
# 연산자 우선규칙을 적용하여 튜플로 인식하지 않음
tn = (99)
print(tn, type(tn)) # 99 <class 'int'>

tx = (10 + 5) * 3
print(tx, type(tx)) # 45 <class 'int'>

#%%

# 2개 이상인 경우는 마지막에 콤마(,) 붙일 필요가 없다.
tl = (1,3,5)      
print(tl)

#%%

# 괄호를 생략할 수 있다.
to = 55,
td = 2,4,6
print(to) # (55,)
print(td) # (2, 4, 6)

#%%

# 한 줄에 여러 변수를 선언할 수 있다.
# 각각의 변수는 튜플이 아니라 
# 개별적으로 지정된 자료형을 갖게된다.
a, b, c, d = 10, 20, 30, 'end'
print(a, type(a)) # int
print(b, type(b)) # int 
print(c, type(c)) # int 
print(d, type(d)) # str





