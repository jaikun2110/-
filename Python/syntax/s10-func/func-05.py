
"""
전역,로컬변수
global, local variable

"""
to=0
def fu(a, b):
    global to
    print("total", to)
    c=a+b
    to+=c
    return c

z=fu(10,20)

print("z=",z)



