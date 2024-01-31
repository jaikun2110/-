# -*- coding: utf-8 -*-

# 반복문 : for
# range(start,end)
# start: 시작값
# end: 종료값, end-1

#%%

# 1부터 10까지 합을 구하라.

start = 1
end = 10 + 1
tot = 0

for x in range(start, end): # x: 1,2,3, ... 10
    # tot = tot + x
    tot += x
    print(f"x({x}), tot({tot})")
    
print(f"최종결과: ({tot})")
    