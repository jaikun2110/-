po={
    "ti": "진달래꽃",
    "au": "김소월",
    "co": "내용"
    
    }

dk=po.keys()#딕셔너리의 키

print(dk)

tk = tuple(dk)

print(po[tk[0]])

va=po.values()#딕셔너리의 값

print(va)

vl=list(po.values())

print(vl[0])

it=list(po.items())

print(it)

ti=it[0]
au=it[1]
co=it[2]
print(ti,au,co)



