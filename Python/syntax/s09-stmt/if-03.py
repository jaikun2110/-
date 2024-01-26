"""
결과 = True if 조건식 else False
조건식이 참이면 True 를 결과에 할당
조건식이 참이 아니면 False를 결과에 할당


"""
"""
문제 점수에 따라 등급을 분류하라
a:90점
b:80점
c:70점
d:60점
e:50점
60점 이상이면 합격 아니면 불합격

"""
s=int(input("점수는 "))
g="등급"
m="여부"
if s>= 90:
    g="A"
    m="합격"
    
elif s>=80:
    
    g="B"
    m="합격"
    
elif s>=70:
    
    g="C"
    m="합격"
elif s>=60:
    g="D"
    m="불합격"
else:
    g="E"
    m="불합격"
    
print(g,m)


#%%
grade="E"
score=int(input())
if score >= 60:
    msg="합격"
    grade = "a" if score>= 90 else \
        "b" if score >= 80 else "e"
else:
    msg="불합격"

