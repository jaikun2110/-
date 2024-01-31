# -*- coding: utf-8 -*-

# 함수 
# 기본값(default value)

# 함수정의
# 기본값을 정의할 때 뒤에서부터 지정
# def move(x=3, y, z):
# def move(x, y=6, z):
def move(x, y=5, z=6):
    print(f"move:x={x}, y={y}, z={z}")
    
#%%

move(10)