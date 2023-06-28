class Node:
    def __init__(self,value,next,index):
        self.value=value
        self.next=next
        self.index=index

class SinglyLinked:
   def __init__(self):
       self.list=None
       self.length=0
   def insert(self,val):
       node=Node(val,self.list,self.length)
       self.list=node
       self.length+=1
   
 
