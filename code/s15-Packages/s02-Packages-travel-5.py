# -*- coding: utf-8 -*-

# 패키지 사용하기 : travel

# from 폴더 import 모듈 as 별칭
# 별칭.클래스(...)

from travel import thailand as tp, vietnam as vp

th = tp.ThailandPackage()
th.detail()

vt = vp.VietnamPackage()
vt.detail()