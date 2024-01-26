"""
가진 돈으로 살수있는 가장 비싼 음료를 구매한다

"""
k=5000
t=3000
w=1000

m=int(input("가진돈?:"))



if m>=k :
    print("5000원 구매함")
elif m>=t :
    print("3000원 구매함")
elif m>=w :
    print("1000원 구매함")
else  :
    print("구매할 수 없음")

"""
논리연산자
or:하나만 참이면 True
and:둘다 참이면 True
not:참이면 False

"""


#%%

m=int(input("가진돈?:"))
k="정수기물"
if (m >= 5000):
    k="커피"
elif (m >= 3000) and (m<5000):
        k="탄산"
elif (m >= 1000) and (m<3000):
            k="물"
print(k)