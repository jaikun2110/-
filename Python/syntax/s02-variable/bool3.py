""" 변수 is 변수 = '==', not 변수 is 변수 = '!='

"""
#%%

a=10
b=20
c=10

q1=a is b
q2=not a is b
q3=a is c
print(q1,'\n', q2,'\n', q3)