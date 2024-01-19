"""[문제] 국어, 영어, 수학 점수의 값을 담을 수 있는 
변수3개를 만들고 총합을 변수로 만들것
"""


lang=30
eng=40
math=50

print(lang+eng+math)

al=lang+eng+math

print(al)


#%%


avg=al / 3

print("평균" , avg)

print("평균" ,al / 3)  #정수 나눗셈
print("평균" ,al // 3) #실수 나눗셈

 print(al) #스페이스바로 띄워놓으면 에러발생
 
 #int= 정수 float=실수