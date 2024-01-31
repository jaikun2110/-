# -*- coding: utf-8 -*-

# 파일 입출력
# open()
# close()
# read(), readline(), readlines()
# write()


#%%

# with : 파일 한 번에 열고 닫기
# with에서 as에 지정된 변수에 객체를 할당하고
# with 블럭을 탈출하면 자동으로 객체를 해제(파일을 닫음)
with open("score-euc-kr.txt", "r", encoding="euc-kr") as score_file:
    while True:
        line = score_file.readline()
        if not line:
            break
        print(line, end="")
    print("[end job]")        

    