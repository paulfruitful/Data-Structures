class Node:
    def __init__(self,value,next,index):
      self.value=value
      self.next=next
      self.index=index

    def delete(self):
      self.next=self.next.next

class SinglyLinked:
   def __init__(self):
      self.list=None
      self.length=0
   def insert(self,value):
      node=Node(value,self.list,self.length)
      self.list=node
      self.length+=1
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
   def remove(self,index):
      self.getIndex(index+1).delete()
      data=self.getIndex(self.length-(index+1))
      self.length-=1
      while data:
         data.index-=1
         data=data.next


   def print(self):
      data=self.list
      res=''
      while data:
         res+=f'{data.index}->{data.value } \n'
         data=data.next
      return print(res)
   


test=SinglyLinked()
test.insert(3)
test.insert(15)
test.insert(25)
test.insert(33)
test.insert(43)
test.insert(83)
test.insert(45)
test.insert(38)
test.insert(37)
test.insert(12)

test.remove(3)
test.print()
