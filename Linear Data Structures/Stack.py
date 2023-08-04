class Stack:
    def __init__(self):
        self.stack=[]
        self.length=0
    def push(self,value):
        self.stack.append(value)
        self.length+=1
    def pull(self):
        self.stack.pop()
        self.length-=1


test= Stack()
test.push(34)
test.push(45)
test.push(23)

test.pull()
print(test.stack)
