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
    def print(self):
        data=self.head
        listed=''
        while data:
            if data.next:
             if data.prev:
              listed+=f'<-{data.val}->'
             else:
                listed+=f'{data.val}->'
            else:
                listed+=f'<-{data.val}'
            data=data.next
        return print(listed)
        
        


test=DoublyLinked()
test.insert(2)
test.insert(3)
test.insert(5)
test.insert(6)
test.insert(8)

test.print()