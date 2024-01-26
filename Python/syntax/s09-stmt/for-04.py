
st=[1,3,5,7,9]

"""
리스트에 들어있는 각 요소에 
100더하여 리스트 만들기

"""

st=[i + 100 for i in st]
print(st)

st2=[i + 100 for i in st]
print(st2)
st3={i + 100 for i in st}
print(st3)
st4=tuple(i + 100 for i in st)
print(st4)
st5=(i + 100 for i in st)
print(type(st5))
for ob in st5:
    print(ob,end=',')
    
#%%
"""
각 요소에 100을 더하여 새로운 리스트를 만들것
리스트 내포 사용금지

"""

ls=[1,3,5,7,9]

lt=[]
for i in ls:
     lt.append(i+100)
print(lt)

#%%

"""
리스트의 홀수 요소만 제곱한 새로운 요소를 만들것
리스트 내포 사용해야함


"""    
lss=[1,2,3,4,5,6]
a=[]
for e in lss:
    if e%3==0:
        a.append(e**2)
    else:
        a.append(e)        
print(a)


