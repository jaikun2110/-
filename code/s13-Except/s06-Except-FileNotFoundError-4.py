# -*- coding: utf-8 -*-

# 예외처리
# 파일이 없는 경우 
# 예외클래스: FileNotFoundError
# 
# finally
# 예외가 발생되든 되지 않든 무조건 실행
# 정상: try 구문을 모두 실행 후 
# 예외: 예외구문 실행 후후


filename = "없는파일-1.txt"
file = None

try:
    file = open(filename, 'r', encoding="UTF8")
    # file = open(filename, 'r')
    print(file)
    data = file.read()
    print(data)
except FileNotFoundError as e:
    print(f"'{filename}'이 존재하지 않습니다.", e)    
finally: # 오류와 상관없이 무조건 실행한다.   
    print("[finally] 파일 닫기")
    # 파일을 찾지 못한 경우 file 변수에 파일객체가 지정되지 않음
    if file != None: 
        file.close()

print("[종료]")