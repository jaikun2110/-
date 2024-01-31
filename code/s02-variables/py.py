# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:34:06 2024

@author: YONSAI
"""

input369=input("삼.육.구!! : ")

print(input369)




def tsnAuto(callNum):
  
    
    for call in range(1, int(callNum)+1):
       k = list(str(call))
       kl =len(k)
       
       
       if(("3" in k )or("6" in k )or("9" in k ) ):
           for lenth1 in range(0,kl):
            
               if(("3" in k[lenth1] )or("6" in k[lenth1] )or("9" in k[lenth1] ) ): print("짝" ,end= "")
           print("\n")   
       else :print(call)     
      
       
  
       
tsnAuto(input369)            
#%%
#while문 이용, 1~100까지 연속으ㅗ 1씩 증가시켜 3의 배수와 5의 배수 구해라.
i=0
three=[]
five=[]
while i<100:
    i = i+1
    if( (i >= 3)and((i % 3) == 0)):
        three.append(i)
    if( (i >= 5)and((i % 5) == 0)):
        five.append(i)

print(three)
print(five)
#%%
import re


counter12 = 0

def t_s_n(counter12 = 0):
    a=input("369 :")
    print(a)
    
    counter12 += 1
    
    if(( a != "짝")&(str(counter12) != a)):
        print("땡!")
        return       
    if((re.match("[369]",str(counter12)) != None)&(a!="짝")):
        print("땡!!!!")
        return 
            
    t_s_n(counter12)
    
t_s_n()

#%%

addList = []

def curculater(a:int,b:int,c:str):

    if(c =="+"):
        addList.append(a+b)
        return a+b
    elif(c=="-"):
        addList.append(a-b if a>b else b-a)
        return a-b if a>b else b-a
    elif(c=="*"):
        addList.append(a*b)
        return a*b
    elif(c=="/"):
        addList.append(a/b)
        return a/b
    elif(c=="total"):
        addList.append((a+b) + ( a-b if a>b else b-a) + (a*b) + (a/b))
        return (a+b) + ( a-b if a>b else b-a) + (a*b) + (a/b)
    elif(c=="average"):
        addList.append(((a+b) + ( a-b if a>b else b-a) + (a*b) + (a/b))/4)
        return ((a+b) + ( a-b if a>b else b-a) + (a*b) + (a/b))/4
    else:
        return f"error: 없는 메서드 호출, {c} 는 없는 메서드입니다. "

def add (a,b):
    addList.append(a+b)
    return a+b
def minus (a,b):
    addList.append(a-b if a>b else b-a)
    return a-b if a>b else b-a
def multiple(a,b):
    addList.append(a*b)
    return a*b
def devide(a,b):
    addList.append(a/b)
    return a/b    
    
def total(a:int,b:int):
    return (curculater(a,b,"+") + curculater(a,b,"-") + curculater(a,b,"*") + curculater(a,b,"/"))
   

def aver(a:int,b:int):
    addList.append(((a+b) + ( a-b if a>b else b-a) + (a*b) + (a/b))/4)
    return ((a+b) + ( a-b if a>b else b-a) + (a*b) + (a/b))/4
    
def printAll(a:int,b:int):
    
    
    print(curculater(a,b,"-"))
    print(curculater(a,b,"*"))
    print(curculater(a,b,"/"))
    print(curculater(a,b,"total"))
    print(curculater(a,b,"average"))
    print(curculater(a,b,"뭐든해봐 "))
    return

def printAll2(a:int,b:int):
    print(add(a,b))
    print(minus(a,b))
    print(multiple(a,b))
    print(devide(a,b))
    print(total(a,b))
    print(aver(a,b))
    
def totalCul():
    cl = [] 
    copyList = cl+ addList
    
    clen = len(copyList)
    
    addAll=0
    for i in range(0,clen):
        addAll = addAll + (copyList[i])
    print(addAll)
def totalCulClear ():
    addList.clear()
    print("clear 완료")
    return        
    
def findHistory(findIndex:int):
   
    copyList = [] + addList
    clen =len(copyList)
    if (findIndex-1) > clen:
        print("err : over index")
        return
    result = copyList[(findIndex-1)]
    print(f"{result} 입니다.")
    return
printAll(20,10)

print("total: " , total(10,2))
print(aver(10,2))
totalCul()
totalCulClear()
printAll2(6, 2)
totalCul()
findHistory(2)
#%%
historyList = []

total2 = [0]

def add2(a,b):
    total2.append(total2[-1] + (a+b))
    historyList.append([a,"+",b,a+b,])
    
    return a+b
def minus2(a,b):
    total2.append(total2[-1] + (a-b))
    historyList.append([a,"-",b, a-b ])
    return a-b
def multiple2(a,b):
    total2.append(total2[-1] + (a*b))
    historyList.append([a,"*",b,a*b])
    return a*b
def devide2(a,b):
    total2.append(total2[-1] + (a/b))
    historyList.append([a,"/",b,a/b])
    return a/b    
def totalCall():
    return total2[-1]

def readHistory(backIndex:int):
    lenH=len(historyList)
    if(backIndex>=lenH):
        return print("err: over index")
    a = historyList[backIndex][0]
    cul= historyList[backIndex][1]
    b =historyList[backIndex][2]
    result=historyList[backIndex][3]
    t=total2[backIndex+1]
        
    return print(f"연산 조회 결과 :{a} {cul} {b} = {result}, 총 연산값 : {t}")

def backToHistory(i:int):
    lenH=len(historyList)
    if(i>=lenH):
        return print("err: over index ")
    copyLH=[]+historyList
    copyLT=[]+total2
    historyList.clear()
    total2.clear()
    for addIndex in range(0,i+2):
        if(addIndex == i+1):
            total2.append(copyLT[addIndex])
            return print("복구 완료 ::", historyList, total2 ,sep="\n")
        historyList.append(copyLH[addIndex])
        total2.append(copyLT[addIndex])
    return print("복구 완료 ::", historyList, total2 ,sep="\n")
        
        
def printAll3(a,b):
    print(add2(a,b))
    print(minus2(a,b))
    print(multiple2(a,b))
    print(devide2(a,b))
    print(totalCall())

def addTotal():
    j= total2[-1]
    i =total2[-1] + total2[-1]
    total2.append(i)
    historyList.append([0,"total",0, total2[-1]])
    return print(f"add total value : + {j}, total : {i}")
def readCurAverage () :
    av=total2[-1] /(len(total2)-1)
    return print(f" total average : {av}")    



printAll3(6, 12)
readHistory(1)

print(historyList)
print("###########")
print(total2)
print("###########")
backToHistory(2)
print("###########")
addTotal()
print("###########")
print(historyList)
print("###########")
print(total2)
print(len(total2))
readCurAverage()


    


    
