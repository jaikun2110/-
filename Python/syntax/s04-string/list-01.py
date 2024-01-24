"""
리스트
여러형태의 자료들의 목록의 연속된 모임
타입 또한 리스트로 나옴

"""

ls=[1,3,5,7,9]
ls1=[2,4,6,8,10]#리스트를 선언하는 2가지

print(ls,type(ls))
print(ls1,type(ls1))

#%%

print(ls[0])#ls의 첫요소
print(ls[-1])#ls의 마지막 요소
print(ls[len(ls)-1])

#%%

#문자열과 달리 리스트는 수정가능

ls[-1]=10
print(ls)