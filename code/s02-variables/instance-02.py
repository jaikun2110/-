# 인스턴스(instance)
#   -> 자료형이 객체(object)화 된 상태
#   -> Return whether an object is an instance of a class 
#      or of a subclass thereof.
#
# 객체(object)
#   -> 고유한 자료의 실체

# 자료형(type)
# pi = 3.14
pi = float(3.14)
# pt = type(pi)       # type(float)
pt = type(3.14)       # type(float)
print(type(pt), pt) # type, float

# isinstance(표현식, type)
# 자료형이 일치하는지 검사하여 
# 결과를 bool(True, False)로 리턴 
print("float?:", isinstance(pi, pt))    # True
print("float?:", isinstance(pi, float)) # True
print("int?:", isinstance(pi, int))     # False
print("str?:", isinstance(pi, str))     # False
print("bool?:", isinstance(pi, bool))   # False

#%%
print("10 / 3 : ", isinstance(10/3, float))   # True
print("10 // 3 : ", isinstance(10//3, float)) # False
print("10 // 3 : ", isinstance(10//3, int))   # True
