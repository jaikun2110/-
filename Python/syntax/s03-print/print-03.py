formet="{0}, {1}"
a="PYTHON"
b="APP"
print(formet.format(a,b))
print(f"{a}과 {b}") 
#f"{변수}텍스트{변수}" 를 이용하여 변수와 텍스트복합출력가능
print("{0}, {1}".format(a, b))
# "{0}{1}.format(변수,변수)" 를 이용하여 변수 삽입 가능
print(a,"과", b, sep=" ")
print(a + "과" + b)

#%%

pa=a + "과" + b
print(pa)

#%%

pb = a
pb +="과"
pb +=b

# (a += b)  =  (a = a + b)
print(pb)



