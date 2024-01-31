
"""
예외처리
파일이 없는 경우
FileNotFoundError
"""
fn="fi.txt"
"""
파일이 없으면 만들어서 리턴해주지 않음
에러발생
"""
file =open(fn,'r')

#%%
fn="fi.txt"
try:
    file =open(fn,'r')
except FileNotFoundError as e:
    print("없는파일",e)
    
#%%
fn="fi.txt"
try:
    file = open(fn,'r')
    data=file.read()
    
except FileNotFoundError as e:
    print("없는파일",e)
    
file.close()
#%%
fn="fi.txt"
file =open(fn,'r')
try:
    file = open(fn,'r')
    data=file.read()
    
except FileNotFoundError as e:
    print("없는파일",e)
else:
    print("else")#정상적으로 처리된 경우 실행됨
finally:#오류가 발생해도 실행됨    
    if file!=None:#파일이 없는 경우 파일객체는 생성되지 않음
        file.close()

