# -*- coding: utf-8 -*-

# 함수 : 가변인자
# 딕셔너리 : dcit
# 인자를 전달할 때 이름을 지정하여 호출하면 딕셔너리로 받을 수 있다.
# 파라미터 : **kwargs, dict로 받음
def move(**kwargs):
    print(f"move({type(kwargs)}) : {kwargs}")
    for key in kwargs.keys():
        print(f"key={key}, val={kwargs[key]}")
    
#%%

move(x=10, y=20, z=30)    
move(a=10, b=20, c=30)    

#%%

# 호출할 때 인자에 키에 해당하는 파라미터를 지정하지 않으면?
# 오류 : TypeError: move() takes 0 positional arguments but 3 were given
# move(10, 20, 30)    

#%%

# 하나의 dict로 호출하면?
# 오류: TypeError: move() takes 0 positional arguments but 1 was given
# move({'x': 10, 'y': 20, 'z':30})

#%%

# 반드시 인자에 파라미터의 이름을 지정해야 한다.
# 인자: 파라미터=값

#%%
move(x={'a': 10})

#%%
move(x={'a': 10}, y={'b':20})

#%%
move(x={'a': 10, 'b':20, 'c':[1,3,5]})

#%%
move(x={'a': 10}, y={'b':20}, c=[1,3,5])
