"""
함수 가변인자
딕셔너리:dict

인자를 전달할 떄 이름을 지정하여 호출하면 
딕셔너리로 받을수 있다

ex)**kwargs
"""

def mo(**kwargs):
   print(type(kwargs),kwargs)
   for ke in kwargs.keys():
    print(ke, kwargs[ke])
    
    
    
    
#%%

mo(x=10,y=20,z=30)


mo(x={'a':10},y=[1,3,5])

mo(x={'a':10, 'b':[1,3,5]})