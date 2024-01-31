"""
with:파일 한번에 열고 닫기

with에서 as에 지정된 변수에ㅐ 객체를 할댕하고
with블럭을 탈출하면 자동으로 객체를 해제=파일.close()
"""

with open("score.txt","r",encoding="utf-8") as sc:
  while True:
    li=sc.readline()
    if not li:
     break
    print(li,end="")    
