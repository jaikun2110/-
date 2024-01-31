# -*- coding: utf-8 -*-

# 함수 : 람다(lambda)
# inline 함수, 익명함수
# 함수형 프로그래밍(functional programming)에 활용
#
# 정의와 선언이 동시에 이루짐
# 정의선언: 함수변수 = lambda 파라미터 : 표현식
# 함수호출: 함수변수(파라미터)
# 결과리턴: 표현식의 처리 결과를 리턴

#%%

# 콜백함수(callback function)
# words: 처리해야 할 데이터
# callback : 데이터를 처리하는 함수로직
# words로 넘어 온 콜랙션 데이터의 첫번째 문자를 대문자로 변환해서 출력
def soundwonder(words, callback):
    for word in words:
        print(callback(word))
        
#%%

words = ['hi', 'good', 'oh', 'nice']

# 일반함수
# 문자열.capitalize() : 첫번째 문자를 대문자로 변환
def wonder(word):
    return word.capitalize() + '!'        

# 첫 번째 문자를 대문자로 바꾸고
# 문자열의 끝에 감탄사(!)를 붙여서 출력
soundwonder(words, wonder)

#%%

# 람다식 함수
# 첫 번째 문자를 대문자로 바꾸고
# 문자열의 끝에 감탄사(!!!)를 붙여서 출력
soundwonder(words, lambda word : word.capitalize() + "!!!")


#%%

soundwonder(['abc', 'test', 'end'], lambda word : word.capitalize() + "!!!")

#%%

# 람다가 처리한 결과를 받음
Hi = (lambda word : word.capitalize() + '!!!')('hi')
print(Hi)
print((lambda word : word.capitalize() + '!!!')('hi'))

#%%

# 람다 함수를 변수로 받음
# 변수에 저장된 함수를 실행해야 결과를 받을 수 있다.
cap = lambda word : word.capitalize() + '!!!'
print(type(cap), cap("good")) # <class 'function'> Good!!!

#%%
