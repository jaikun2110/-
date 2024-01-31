class BirdException(Exception):
    def __init__(self,errno,msg='',why=''):
        super().__init__(msg)
        self.errno=errno

    def why(self):
        return self.why
    
et=Exception()

def HiBird(hi):
        if hi=='dead':
         raise BirdException(-1,"새가죽음","늙어서")
        print("반갑습니다")
        
try:
    HiBird('dead')
except BirdException as e:
    print("errno",e.errno)
    print("why",e.why)
    print("args",e.args)