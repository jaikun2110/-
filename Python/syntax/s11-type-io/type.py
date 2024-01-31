
#함수인자와 반환값에 대한 복합타입 어노테이션

from ty import li
def sum_elements(numbers:li[int]) ->int:
    return(numbers)
print(sum_elements([1,3,5,7,9]))

#%%

def printx(msg:str) -> none:
    print(msg)
    
printx("리턴이 없는값 호출")