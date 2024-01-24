
"""
리스트에서 해당하는 값을 포함하는 갯수 세기:cound()

갯수:리스트.cound(값)
리턴 : 해당하는 값과 일치하는 요소의 갯수

"""
lst =  ['삼성','sk', 'lg']

value='lg'
count=lst.count(value)

print(f'{lst}.count({value})',count)

#%%

value='ibm'
count=lst.count(value)
print(f'{lst}.count({value})',count)#없으면 0이 출력 됨