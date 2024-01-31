# 딕셔너리 결합(update)
# 기존의 딕셔너리에 새로운 딕셔너리를 결합
# dict.update(newdict)

weeks = {1:'월', 2:'화', 3:'수', 4:'목', 5:'금', 6:'토'}

print('월요일:', 1 in weeks) # True
print('일요일:', 7 in weeks) # False

#%%

sun = {7: '일'}

weeks.update(sun)

print('일요일:', 7 in weeks) # True

#%%

# TypeError: unsupported operand type(s) for +=: 'dict' and 'dict'
# weeks += sun
# weeks = weeks + sun

