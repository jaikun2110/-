# -*- coding: utf-8 -*-

# 패키지 사용하기 : travel

# 사용불가: 폴더.모듈.클래스
# ModuleNotFoundError: No module named ...
# import travel.thailand.ThailandPackage

# from 폴더.모듈 import 클래스
# 사용할 때 폴더.모듈 생략하고 클래스 이름 직접 사용
from travel.thailand import ThailandPackage

th = ThailandPackage()
th.detail()

#%%

from travel.vietnam import VietnamPackage
vt = VietnamPackage()
vt.detail()