class Node:
    def __init__(self,val,next,prev,index):
        self.val=val
        self.next=next
        self.prev=prev
        self.index=index
class DoublyLinked:
    def __init__(self):
        self.head=None
        self.length=0
    def insert(self,value):
        node= Node(value,self.head,None,self.length)
        if self.head:
            self.head.prev=node
        self.head=node
        self.length+=1


test=DoublyLinked()
test.insert(2)
test.insert(3)
print(test.head.next.prev.val)