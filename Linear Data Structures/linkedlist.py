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
   def checkIfExists(self,val):
      data=self.list 
      ans='Not Found'   
      while data:
         if data.value==val:
            ans='Found'
            break
         else:
            data=data.next
      return ans
   def getNode(self,index):
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
      self.getNode(index+1).delete()
      data=self.list
      self.length-=1
      while data:
         if data.index<index:
            break
         
         data.index-=1
         data=data.next


   def print(self):
      data=self.list
      res=''
      while data:
         if data.next != None:
          res+=f''' {'{'}\nIndex:{data.index},\nValue:{data.value },\nNext:{data.next.value}\n{'}'}\n \n'''
         else:
            
          res+=f''' {'{'}\nIndex:{data.index},\nValue:{data.value },\nNext: Null\n{'}'}'''
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
print(test.checkIfExists(33))
