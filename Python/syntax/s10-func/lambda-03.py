
"""
콜백함수
words:처리해야할 데이터
callback:데이터를 처리하는 함수로직
words로 넘어온 콜렉션 데이터의 첫번째 문자는
대문자로 변환되어 출력 됨
"""

def su(words,callback):
    for word in words:
        print(callback(word))
        
        
#%%
words = ['hi','good','oh','nice']


def won(word):
    return word.capitalize()+'!'
#첫번째 문자를 대문자로 바꾸고 !를 붙여서 출력

su(words, won)

#%%

"""
람다식 함수
첫번째 문자를 대문자로 바꾸고
문자열 끝에 감탄사"!!!" 를 붙여서 출력


"""
def so(wo, callback):
    for word in wo:
        print(callback(word))


wo = ['hi','good','oh','nice']
so(wo,lambda word : word.capitalize() +'!!!')


    