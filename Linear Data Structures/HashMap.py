#The HashMap Direct Chaining Implement

class HashMap:
    def __init__(self,size):
        self.size=[0] * size
    
    def hasher(self,arg):
        return arg % 345
    
        


test=HashMap(10)


print(test.hasher(1000))