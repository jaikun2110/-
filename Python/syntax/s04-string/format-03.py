
n=12345
s="helo"
f=0.12345

print(f"정수 : ({n:>10})")
print(f"정수 : ({n:<10})")
print(f"정수 : ({n:>10d})")



print(f"실수 : ({f:>10})")
print(f"실수 : ({f:<10})")
print(f"실수 : ({f:<10.3})")
print(f"실수 : ({f:>10.3})")
print(f"실수 : ({f:<10.3f})")


print(f"문자열 : ({s:<10})")#좌측정렬
print(f"문자열 : ({s:>10})")#우측정렬
print(f"문자열 : ({s:^10})")#중앙정렬

#%%

print("정수 중앙정렬({0:^10})".format(n))


print("전체 중앙정렬({0:^10})({1:^10})({2:^10})".format(n,f,s))
print("전체 중앙정렬({n})({f})({s})")
print("전체 중앙정렬({})({})({})".format(n,f,s))


#%%

name="길동"
age=35

msg = "이름{0}   나이 {1} ".format(name, age)

print(msg)

fmt= "이름{0}   나이 {1} "

print(fmt.format(name, age))



