# -*- coding: utf-8 -*-
# if문

# 조건부 표현식(conditional expression)
# 결과 = '참' if 조건식 else '거짓'

# 조건식이 참이면 '참'을 결과에 할당
# 조건식이 참이 아니면 '거짓'을 결과에 할당

#%%
# [문제]
# 점수(score)에 따라 등급을 분류하라.
# A: 90점 이상
# B: 80점 이상
# C: 70점 이상
# D: 60점 이상
# E: 60점 미만
# 60점 이상 '합격'
# 60점 미만 '불합격'

score = 59  # 점수
grade = 'E' # 등급
msg = '불합격' # 합격 or 불합격

#%%
# 처리:
    
if score >= 60:
    msg = '합격'
    grade = 'A' if score >= 90 else \
        'B' if score >= 80 else \
        'C' if score >= 70 else 'D'
    
#%%
# 결과:
print(f"점수({score}), 등급({grade}), 합격유무({msg})")    
