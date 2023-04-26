class Node:
    def __init__(self,value,next,index):
      self.value=value
      self.next=next
      self.index=index
      
    def delete(self):
      self.next=self.next.next

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
   def remove(self,index):
      self.getIndex(index+1).delete()

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
      string='\n Circular Linked List'
      while data:
         if data.index== (0):
            string+=f'''
        ------------------------- 
        index:{data.index}
        value: {data.value}
        next:({data.next.value})
        -------------------------
        '''
            break
       
         else:
             string+=f'''
        ------------------------- 
        index:{data.index}
        value: {data.value}
        next:({data.next.value})
        -------------------------
         |
        \ /
        '''
             data=data.next.next
      return print(string)
   

test=CircularLinked()
test.insert(3)
test.insert(13)
test.insert(23)
test.insert(33)
test.insert(43)


test.print()