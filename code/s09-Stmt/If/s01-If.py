# 제어문 : if
"""
if 조건식:
    실행문(조건식이 만족하는 경우)
elif 조건식:
    실행문, 생략가능 
    상위 조건식이 만족하지 않고
    해당 조건식이 만족하는 경우 
else:
    실행문(조건식이 만족하지 않는 경우), 생략가능
"""    
# 블럭(block)
#   - 블럭의 시작은 콜론(:)
#   - 들여쓰기로 구분(indent)
#   - Tab : 기본 8자리이지만 에디터에서 설정 가능
#   - Space : 공백문자도 가능

#%%

weather = '비'    

# weather의 값이 '비'라는 값과 같은가?
if weather == '비':
    print('우산을 챙기세요.')
    print('그리고 반드시 가져오세요.')


#%%

weather = '맑음'    

# weather의 값이 '비'라는 값과 같은가?
if weather == '비':
    print('우산을 챙기세요.')
    print('그리고 반드시 가져오세요.')

print("종료")

#%%

weather = '미세먼지'    

if weather == '비':
    print('우산을 챙기세요.')
    print('그리고 반드시 가져오세요.')
elif weather == '미세먼지': # else if
    print('마스크를 챙기세요')

print("종료")

#%%

weather = '맑음'    

if weather == '비':
    print('우산을 챙기세요.')
    print('그리고 반드시 가져오세요.')
elif weather == '미세먼지': # else if
    print('마스크를 챙기세요')
else: # 위의 모든 조건식이 만족하지 않으면
    print("준비물이 필요 없어요.")
    
print("종료")

#%%

weather = '맑음'    

if weather == '비':
    print('우산을 챙기세요.')
    print('그리고 반드시 가져오세요.')
elif weather == '미세먼지': # else if
    print('마스크를 챙기세요')
elif weather == '맑음': 
    print("준비물이 필요 없어요.")
    
print("종료")

#%%

# weather = None
weather = ''

if weather == '비':
    print('우산을 챙기세요.')
    print('그리고 반드시 가져오세요.')
elif weather == '미세먼지': # else if
    print('마스크를 챙기세요')
elif weather == '맑음': 
    print("준비물이 필요 없어요.")
else:
    print("모르겠습니다.")    
    
print("종료")

