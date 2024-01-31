# -*- coding: utf-8 -*-

# 예외처리
# 파일이 없는 경우 
# 예외클래스: FileNotFoundError

filename = "없는파일-1.txt"

try:
    # file = open(filename, 'r', encoding="UTF8")
    file = open(filename, 'r')
    print(file)
    data = file.read()
    print(data)
    # read()에서 예외가 발생하면 close() 되지 않고 진행
    # file.close() 
except FileNotFoundError as e:
    print(f"'{filename}'이 존재하지 않습니다.", e)    

# open()에서 오류가 나오면 
# 예외발생: NameError: name 'file' is not defined
try:
    file.close()
except:
    pass

print("[종료]")