class Bird:
    def fly(self):
       raise NotImplementedError()
       
       
class Eagle(Bird):
    def fly(self):
       print("날다")
       
eagle=Eagle()
eagle.fly