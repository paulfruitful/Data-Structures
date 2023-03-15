class Node:
  def __init__(self, value,next,index):
    self.value=value
    self.next=next
    self.index=index

class SinglyLinked:
  def __init__(self):
    self.list=None
    self.length=0
  def insert(self,value):
    node=Node(value,self.list,self.length)
    self.list=node
    self.length+=1
  def find(self,value):
    data=self.list
    ans=f'{value} Not Present'
    while data:
      if data.value==value:
         ans=f'{value} Present'
         break  
      else:
        data=data.next
    return print(ans)
  
  def getIndex(self,index):
      data=self.list
      ans='That Index Is Not Available'
      while data:
        if data.index==index:
           ans=data
           break
        else:
          data=data.next 
      return ans  
  

test=SinglyLinked()
test.insert(23)
test.insert(20)
indexed=test.getIndex(4)
print(indexed)

