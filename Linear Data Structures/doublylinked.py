class Node:
    def __init__(self,val,next,prev,index):
        self.val=val
        self.next=next
        self.prev=prev
        self.index=index

    def delete(self):
      self.next=self.next.next
      self.next.prev=self


class DoublyLinked:
    def __init__(self):
        self.head=None
        self.length=0
    def insert(self,value):
        node= Node(value,self.head,None,self.length)
        if self.head:
            self.head.prev=node
        self.head=node
        self.length+=1
    def print(self):
        data=self.head
        listed=''
        while data:
            if data.next:
             if data.prev:
              listed+=f'''
                      / /
                       |
                ---------------
                next: {data.next.val}
                value:{data.val}
                index:{data.index}
                prev: {data.prev.val}
                ------------------
                    |
                   \ /
                '''
             else:
                listed+=f'''
                ---------------
                next: {data.next.val}
                value:{data.val}
                index:{data.index}
                prev: Null
                ------------------
                    |
                   \ /
                '''
            else:
                listed+=f'''
                       / /
                        |
                ---------------
                next: Null
                value:{data.val}
                index:{data.index}
                prev:{data.prev.val}
                ------------------
                '''
            data=data.next
        return print(listed)
    def find(self,val):
      data=self.head
      ans='Not Found'   
      while data:
         if data.val==val:
            ans='Found'
            break
         else:
            data=data.next
      return ans
    def getIndex(self,index):
       data=self.head
       while data:
          if data.index==index:
             break
          else:
             data=data.next
       if data:
        return data
       else:
          return 'Index Not Found'
       
    def remove(self,index):
      self.getIndex(index).prev.delete()
      data=self.head
      self.length-=1
      while data:
         if data.index<index:
            break
         
         data.index-=1
         data=data.next

       
        


test=DoublyLinked()
test.insert(2)
test.insert(3)
test.insert(5)
test.insert(6)
test.insert(8)
test.remove(3)
print(test.find(6))

