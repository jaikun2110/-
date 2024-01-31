# -*- coding: utf-8 -*-

# 예외처리
# 파일이 없는 경우 
# 예외클래스: FileNotFoundError

# 절대경로 지정
# filename = "e:/Temp/없는파일.txt"

# 상대경로 지정: 실행코드가 있는 폴더
# filename = "./없는파일.txt"
filename = "없는파일.txt"

# 파일이 없으면 객체를 만들어서 리턴해 주지 않으며
# 예외가 발생: FileNotFoundError
# FileNotFoundError: [Errno 2] No such file or directory: '파일이름'
file = open(filename, 'r')
print(file) # TextIOWrapper