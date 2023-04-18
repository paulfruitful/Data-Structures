class Node:
    def __init__(self,value,next,index):
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
     def rem(list,ind):
        if list== None:
           return
        if ind==list.index:
           list=list.next
        rem(list.next,ind)
     rem(self.list,index)

       

   def print(self):
      data=self.list
      while data:
         print(f'{data.index}->{data.value },')
         data=data.next
   

test=SinglyLinked()
test.insert(3)
test.insert(13)
test.insert(23)
test.insert(33)
test.insert(43)

test.remove(0)
test.print()