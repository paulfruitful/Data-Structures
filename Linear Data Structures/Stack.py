class Stack:
    def __init__(self):
        self.stack=[]
        self.lenght=0
    def push(self,value):
        self.stack.append(value)
        self.length+=1
    def pull(self):
        self.stack.pop()
        self.length-=1
