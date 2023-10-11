class Node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self) -> None:
        self.root=None
        self.size=0

    def insert(self,data):
      if self.root==None:
            self.root=Node(data)
            self.size+=1
            
      else:
       self.help_insert(data,self.root)


    def help_insert(self,data,root):
         if root.value<data:
            if root.right is None:
                root.right=Node(data)
                self.size+=1
            else:
             self.help_insert(data,root.right)
        
         if root.value>data:
            if root.left is None:
                root.left=Node(data)
                self.size+=1
            else:
             self.help_insert(data,root.left)


    def getNode(self):
        if self.root is None:
            return
        

test=Tree()
test.insert(3)

test.insert(8)
print(test.root.left)