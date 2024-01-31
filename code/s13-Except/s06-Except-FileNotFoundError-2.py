# -*- coding: utf-8 -*-

# 예외처리
# 파일이 없는 경우 
# 예외클래스: FileNotFoundError

filename = "임시파일.txt"

try:
    file = open(filename, 'r')
except FileNotFoundError as e:
    print(f"'{filename}'이 존재하지 않습니다.", e)    
