# 나머지 : %
# 몫과 나머지 : divmod(x,y)

a = 10 
b = 3
m = a % b
print(f"{a}를 {b}로 나눈 나머지는?", m) # 1

#%%

# 몫과 나머지 : 튜플(tuple)
g = divmod(a, b)
print(f"{a}를 {b}로 나눈 몫과 나머지는?", g) # (3, 1)

# 몫과 나머지를 분리(unpacking)
gm, gn = g
print(f"{g}에서 몫({gm})과 나머지({gn})로 분리")

#%%

print(f"{g}에서 몫({g[0]})과 나머지({g[1]})로 분리")

#%%

g1 = a // b     # 몫: 10 // b -> 3
g2 = a - g1 * b # 나머지: 10 - (3 * 3)

print(f"{a, b}에서 몫({g1})과 나머지({g2})로 분리")



