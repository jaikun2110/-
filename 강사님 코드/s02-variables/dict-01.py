# -*- coding: utf-8 -*-
"""
# 딕셔너리
# 키와 값으로 구성된 자료형
# 파이선의 표기 : dict
# {키1:값1 ...}

########################################
# 키는 특정 해시(hash)로 만들어진다.
# 특징 : 장1: 검색속도 빠름
#       단1: 용량을 많이 차지 
#       단 2: 순차적으로 처리하는 속도가 느리다.
# 키는 불변값을 써야 함 
#   -list를 키로 사용할 수는 없음
#    - 중복 허용 X

# hash: 메모리 상의 공간에서 컴퓨터가 자료를 가지기 위해 key와 value를 매핑해서 데이터를 저장하는 구조 
   

"""
#%%
# 키참조: dict[키]
# 기본형
dict1:dict = {
    "title": "dict1",
    "author":"choi",
    "content":"decription of dict"
}
print(dict1)
print(dict1["title"], dict1["author"], dict1["content"], sep=", ")

#%%

# Add New Data
# 키가 있으면 찾아서 그 것을 바꿔주고, 없으면 추가
dict1["annotation"] = "# 이거 json이랑 굉장히 구조가 유사한데?"
dict1["author_info"]="age :31"
print(dict1["annotation"], dict1["author_info"], sep=", ")
dict1["author_info"]="age : 1994년생"
print( dict1["author_info"], sep=", ") 
#%%
# del : 삭제

del dict1["annotation"]

# get의 경우, 인자를 두 개 받는데, 인자에 이름을 넣어서 구분하지 않음: default=""시 타입에러
print(dict1.get("annotation", "이거 없어요" )) # 없으니까 2번째 인자 출력
#%%

def poetry():
    poemList:dict = {
        "poem1"  : """
        승무
                        조지훈
        
        얇은 사 하이안 고깔은 
        고이 접어 나빌레라

        파르라니 깎은 머리
        박사 고깔에 감추오고,

        두 볼에 흐르는 빛이
        정작으로 고와서 서러워라.

        빈 대에 황촉불이 말 없이 녹는 밤에
        오동잎 잎새마다 달이 지는데,

        소매는 길어서 하늘은 넓고
        돌아설듯 날아가며 사뿐이 접어 올린 외씨 버선이여.

        까만 눈동자 살포시 들어
        먼 하늘 한개 별 빛에 모두오고,

        복사꽃 고운 뺨에 아롱질듯 두 방울이야
        세사에 시달려도 번뇌는 별빛이라.

        휘어져 감기우고 다시 접어 뻗는 손이,
        깊은 마음 속 거룩한 합장인 양하고, 

        이 밤사 귀또리도 지새우는 삼경인데
        얇은 사 하이얀 고깔은 고이 접어 나빌레라.
        
        

        """ ,
        "poem2" : """
        귀천
                                천상병
                    
        나 하늘로 돌아가리라.
        새벽빛 와 닿으면 스러지는
        이슬 더불어 손에 손을 잡고
        
        나 하늘로 돌아가리라
        노을빛 함께 단 둘이서
        기슭에서 놀다가 구름 손짓하면은
        
        나 하늘로 돌아가리라
        아름다운 이 세상 소풍 끝내는 날
        가서, 아름다웠더라고 말하리라....
        
            
        """,
        "poem3" :"""
        편지
                    김소월
        누나
        이 겨울에도
        눈이 왔읍니다
        흰 봉투에
        눈을 한 줌 넣고
        글씨도 쓰지말고
        우표도 붙이지 말고
        말쑥하게 그대로
        편지를 부칠까요?
        누나 가신 나라엔
        눈이 아니온다기에
        
        
        """,
        
        
        }
    poem_scanner=input("1~3 : ")
    
    print(poem_scanner)
    poe = f"poem{poem_scanner}"
   # if(poem_scanner=="1"):
   #     print(poemList["poem1"])
   # elif(poem_scanner=="2"):
   #     print(poemList["poem2"])
   # else: print(poemList["poem3"])
   
    print(poemList[poe])
    
    
    return

poetry()
#%%

#%%%
def scoreListener(score):
    if(score <0):
        print("error")
        return
    if(score>=90):
        print("grade A")
    elif(score>=80):
        print("grade B")
    elif(score>=70):
        print("grade C")
    elif(score>=60):
        print("grade D")
    elif(score>=50):
        print("grade E")
    else:print("불합격")
    return


a1 = input("몇 점이신가요? :")
print(a1)
b=int(a1)
scoreListener(b)





#%%
s=0
for i in range(1,11):
    
    s = s+ i 
print(s)

#%%
total=0
odd=0
even=0
for i in range (1,11):   
   if(i%2) != 0: odd += i       
   else: even = even + i
   total +=i
   
print (odd , even, total)
#%%
k=0
for i in range (1,11,2):   
    k += i
    

print("1~10 odd 합 :",k)

#%%
#문제: 구구단 2단~9단, for문



t = input("구구단 보고싶은 단 수를 입력, 자연수 1 ~ n :")



def 구구단 (n) :
    
    for i in range(1,10):
        
        print(f"{n} 곱하기 {i}는 ", n*i)
    

    
구구단(int(t))


#%%

for i in range(2,10):
        for k in range(1,10):
            print(f"{i}*{k} :", "%2d" %(i*k), end=" ")
        print(f"{i} 단 끝")
        











































    
