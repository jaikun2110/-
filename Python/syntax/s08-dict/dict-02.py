"""
키 참조:dict[키]


"""

po={
    "ti": "진달래꽃",
    "au": "김소월",
    "co": "내용"
    
    }

print(po)

ti=po['ti']
au=po['au']
co=po['co']
#= co=po.get('co')
#변수로 존재하지 않는 딕셔너리 키를 참조하면 에러 발생
#co=po.get('co') 겟을 이용하면 에러 발생X
#co=po.get('co','123') 으로 사용시 co 키를 생성하며 
#123값이 입력됨

print(ti,au,co,sep='\n')

po['age'] = 34
#딕셔너리 키 추가
print(po)

po['age'] = 36
#딕셔너리 값 변경
print(po)

del po['age']
#딕셔너리 키와 값 삭제
print(po) 