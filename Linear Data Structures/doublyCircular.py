class Node:
     def __init__(self,val,next,prev,index):
        self.value=val
        self.next=next
        self.prev=prev
        self.index=index
        
     def delete(self):
      self.next=self.next.next
      self.next.prev=self
      

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
      first=self.getNode(0)
      first.next=node
      self.list.prev=first

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
      self.getNode(index+1).delete()

   def print(self):
      data=self.list
      string='\nDOUBLY CIRCULAR LINKED LIST'
      while data:
        if data.index!=0:
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
         
        
        data=data.next
      return print(string)
   def remove(self,index):
      self.getNode(index).prev.delete()
    
      self.length-=1
   
   

test=CircularLinked()
test.insert(1)
test.insert(2)

