# -*- coding: utf-8 -*-
# if문

# 결과 = '참' if 조건식 else '거짓'
# 조건식이 참이면 '참'을 결과에 할당
# 조건식이 참이 아니면 '거짓'을 결과에 할당

#%%

score = 59
if score >= 60:
    msg = '합격'
else:
    msg = '불합격'    
    
print(f"당신의 점수는 ({score})점이며 ({msg})입니다.")    

#%%

score = 77

msg = '합격' if score >= 60 else "불합격"
print(f"당신의 점수는 ({score})점이며 ({msg})입니다.")    
