


x=10
y=0

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