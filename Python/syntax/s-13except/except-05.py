l=[0,10,2,3,4]
print(l[0,l[4]])

print(l[6])

"""
index error

"""




try:
    print("x=",x)
    print("y=",y)
    print("z=",z)
    z=x/y
    
except ZeroDivisionError as e:
    print("예외발생",e)

except NameError as e:
    print("예외발생",e)    

"""
except:
    print("예외발생")
= 모든예외처리
"""
print(x,y,z)