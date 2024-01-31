# -*- coding: utf-8 -*-

# 예외처리
# 파일이 없는 경우 
# 예외클래스: FileNotFoundError
# 
# finally
# 예외가 발생되든 되지 않든 무조건 실행
# 정상: try 구문을 모두 실행 후 
# 예외: 예외구문 실행 후후


filename = "없는파일.txt"

try:
    file = open(filename, 'r', encoding="UTF8")
    print(file.read())
except FileNotFoundError as e:
    print("[예외발생] ", e)    
else: # 옵션: 예외가 발생되지 않고 정상적으로 처리한 경우
    print("[else] 파일 닫기")
    file.close()
finally: # 옵션: 오류와 상관없이 무조건 실행한다.   
    print("[finally] 마무리 작업")

print("[종료]")