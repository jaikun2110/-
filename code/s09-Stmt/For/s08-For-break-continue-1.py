# -*- coding: utf-8 -*-

# 반복문 : for
# 흐름제어 : continue, break

# break
# 자신이 속한 해당 블록문을 탈출
for n in range(100):
    print('n=', n)
    if n >= 10:
        break # 탈출

print('마지막 처리 숫자', n)


#%%

for x in range(10):
    print('x=', x)
    for y in range(100, 200, 5):
        print('y=', y)
        if y > 110:
            break; # y 블록만 탈출
        
    print('종료:y')        
        



#%%

# continue
# 다음 명령문을 실행하지 않고 
# 반복문의 시작 위치로 이동한다.

for n in range(10): 
    if n % 2 == 1: # 홀수
        print("n=", n, 'continue')
        continue
    print('n=', n) # 짝수만 출력


#%%

even = 0

for n in range(10): 
    if n % 2 != 1: # 짝수, 홀수가 아니면
        even += n
        print('n=', n) # 짝수만 출력

print('짝수의 합:', even)    

