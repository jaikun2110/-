# -*- coding: utf-8 -*-

# [문제]
# 리스트 내포를 사용하여 구구단을 작성하라.

result = [m * n for m in range(2,10)
          for n in range(1,10)]

print(result)

