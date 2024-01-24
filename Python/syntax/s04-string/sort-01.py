"""
리스트 정렬: sort
오름차순(ascending):작은값에서 큰값
내림차순

원본이 변경됨 요소의 위치가 바뀜
"""


score =[90,80,70,60,50,40]


score.sort()

print(score)#기본값은 오름차순

score.reverse()
#sort()로 오름차순 정렬후 reverse()로 반전되어 내림차순으로 변경됨

print(score)


sc =['one','two','three','four']

sc.sort()#문자는 아스키코드값 순서로 나ㅏ옴

print(sc)

slt=[3,'삼',4.1]

slt.sort()#자료형이 다른경우 정렬불가
#%%
"""
리스트에서 요소 꺼내기:pop()
꺼낸요소는 삭제됨
"""

lst=['lg','sk','sam']

print(lst.pop(0))
print(lst.pop(1))

print(lst)

#%%
lst=['lg','sk','sam']
ind=2#인덱스 범위를 넘어서면 예외처리 됨
va=lst.pop(ind)
print(f"{lst}.pop({ind}) , {va}")


