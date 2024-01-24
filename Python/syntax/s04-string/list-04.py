

lst=['이름',8,9,10]


sc=lst[1]#call by value :리스트 값을 변수에 지정
print('t\숫자:',lst)

#%%

sc[0] = 88

print(lst)#리스트는 변경 가능

#%%


sl = lst[1:]
sl = sl[0]
sl[1] = 99
print(sl)