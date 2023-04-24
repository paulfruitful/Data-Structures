class Node:
     def __init__(self,val,next,prev,index):
        self.value=val
        self.next=next
        self.prev=prev
        self.index=index
        
     def delete(self):
      self.next=self.next.next

class CircularLinked:
   def __init__(self):
      self.list=None
      self.length=0
   
   def insert(self,value):
      node=Node(value,self.list,None,self.length)
      if self.list:
            self.list.prev=node
      self.list=node
      self.length+=1
      first=self.getIndex(0)
      first.next=node
      self.list.prev=first

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
   def remove(self,index):
      self.getIndex(index+1).delete()

   def print(self):
      data=self.list
      string='\nDOUBLY CIRCULAR LINKED LIST'
      while data:
        
        string+=f'''
        -------------------------
        prev: ({data.prev.value})
        index: {data.index}
        value: {data.value}
        current ({data.next.value})
        -------------------------
         |
        \ /
        '''
        if data.index==0:
            string+=f'''
        ------------------------
        prev: ({data.prev.value})
        index: {data.index}
        value: {data.value}
        next: ({data.next.value})
        ---------------------------
        '''
            break
         
        data=data.next.next
      return print(string)
   def remove(self,index):
      self.getIndex(index+1).delete()
      data=self.list
      self.length-=1
      while data:
         if data.index<index:
            break
         else:
          data.index-=1
          data=data.next
   

test=CircularLinked()
test.insert(3)
test.insert(13)
test.insert(23)
test.insert(33)
test.insert(43)
test.getIndex(2).delete()
