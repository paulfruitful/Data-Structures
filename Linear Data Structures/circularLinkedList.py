class Node:
    def __init__(self,value,next,index):
      self.value=value
      self.next=next
      self.index=index

class CircularLinked:
   def __init__(self):
      self.list=None
      self.length=0
   def insert(self,value):
      node=Node(value,self.list,self.length)
      self.list=node
      self.length+=1
      first=self.getIndex(0)
      first.next=node
   def find(self,val):
      data=self.list
      ans='Not Found'   
      while data:
         if data.value==val:
            ans='Found'
            break
         else:
            data=data.next
      return ans
   def getIndex(self,index):
      data=self.list
      ans='Index Not Found'
      while data:
         if data.index==index:
            ans=data
            break
         else:
            data=data.next
      return ans
   
   def print(self):
      data=self.list
      string=''
      while data:
         string+='f{data.val}->{data.next.val}->'
         data=data.next.next
      return print(string)
   

test=CircularLinked()
test.insert(3)
test.print()