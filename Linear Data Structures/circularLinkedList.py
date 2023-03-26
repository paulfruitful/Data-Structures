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
   
      while data:
         if data.index==index:
            break
         if data.index==0:
            break
         else:
            data=data.next 
      if data.index==index:
       return data
      else:
         return 'Index Not Found'
   
   def print(self):
      data=self.list
      string=''
      while data:
         string+=f'{data.value}->{data.next.value}->'
        
         if data.index== (0):
            string+=f'{data.value}->({data.next.value})'
            break
         else:
             data=data.next.next
      return print(string)
   

test=CircularLinked()
test.insert(3)
test.insert(13)
test.insert(23)
test.insert(33)
test.insert(43)
test.print()
print(test.getIndex(100))