# ESCAPE Character
# 백슬래시(\) 기호를 사용
# raw string(이스케이프 문자를 무시)

#%%

# 무시 : \n, \t
print(r"He is always saying \nCould you say is again?")
print(r"He is always saying \tCould you say is again?")

# 예외 : 
# 문자열의 끝인 경우 \"에 오는 문자를 그대로 해석해서
# 문자열 종료가 없는 것으로 인식
# SyntaxError: unterminated string literal 
# print(r"He is always saying \Could you say is again?\")
print(r"He is always saying \Could you say is again?\ ")
