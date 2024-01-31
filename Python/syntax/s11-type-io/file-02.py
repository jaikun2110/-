"""
파일 입출력
open()
close()
read(),readline(),readlines()
write()
"""
#'w' 새로운 파일 생성
sc=open("score.txt","w",encoding="utf-8")
print("수학88",file=sc)


sc.close()
#%%
#'a' 기존파일에 추가
sc=open("score.txt","a",encoding="utf-8")
print("국어88",file=sc)
#= sc.write("국어88",\n)

sc.close()

#%%
#'r'
#파일객체.read():파일의 데이터를 읽어서 리턴
#파일을 읽기모드로 오픈
sc=open("score.txt","r",encoding="utf-8")
rd=sc.read()
print(rd)
sc.close()

#%%

"""
파일을 라인단위로 읽기
파일객체.readline()

"""
sc=open("score.txt","r",encoding="utf-8")

da1=sc.readline()#첫번째 라인을 읽어옴

print(da1)
sc.close()


#%%

#한 라인씩 모두 불러오기
sc=open("score.txt","r",encoding="utf-8")

while True:
    line=sc.readline()
    if not line:
        print("empty",line)
        break
    print(line,end="")    
sc.close()



#%%


sc=open("score.txt","r",encoding="utf-8")

lis=sc.readline()
print(len(lis),lis)
#

sc.close()
