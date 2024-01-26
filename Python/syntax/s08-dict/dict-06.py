
we={1:'월',2:'화',3:'수'}

print(1 in we)
print(4 in we)

#%%

su = {4:'목'}

we.update(su)
#딕셔너리는 연산자 지원 안되므로 update() 사용

print(4 in we)