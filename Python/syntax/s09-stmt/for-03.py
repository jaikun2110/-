"""
반복문:for

딕셔너리 활용



"""


co={
    '1층':'전시',
    '2층':'매장',
    '3층':'사무',
    '4층':'통제실'
    }

for ke in co:#값을 제외한 키값만 꺼내옴
    print(ke)
    
#%%

for ke in co.keys():#co.values() 를 사용하면 값을 꺼내옴
    print(ke)
    
    
for it in co.items():
    ke,va=it
    print(ke)
    print(it)
#%%
for ke,va in co.items():
    print(f"{ke}:{va}")
    
#%%

for ke in co.keys():
    print(f"{ke}:",co[ke])
    
    
#%%

ls=[('1층','전시'),
    ('2층','매장'),
    ('3층','사무'),
    ('4층','통제실')
    ]

for k,v in ls:
    print(k,v)