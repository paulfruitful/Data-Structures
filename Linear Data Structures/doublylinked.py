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
    def insert(val):
        node= Node(val,self.head,None,self.length)
        if not self.head:
            self.head.prev=node
        self.length+=1
        
