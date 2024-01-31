# -*- coding: utf-8 -*-

# 파일 입출력
# open()
# close()
# read(), readline(), readlines()
# write()

#%%

# 'w' : 새로운 파일을 생성, 기존 파일은 덮어쓰기
score_file = open("score.txt", "w", encoding="utf8")
print("수학: 77", file=score_file)
print("영어: 88", file=score_file)
score_file.close()

#%%

# 'a': 기존 파일에 추가, 없으면 새로운 파일을 생성
score_file = open("score.txt", "a", encoding="utf8")
print("국어: 99", file=score_file)
print("역사: 90", file=score_file)
score_file.close()

#%%

# 'w' : 새로운 파일을 생성, 기존 파일은 덮어쓰기
score_file = open("score.txt", "w", encoding="utf8")
score_file.write("수학: 90\n")
score_file.write("영어: 92\n")
score_file.close()


