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

    
    def minNode(self,node):
       if(not node.left):
          return node
       else:
          self.minNode(self,node.left)
    
    def delete(self,value):
       self.root=self.__help_delete(self.root,value)

    def __help_delete(self,root,value):
       if(root.value==value):
          if(root.right==None and root.left):
             root=root.left 
             return root
          elif(root.right and root.left==None):
             root=root.right
             return root
          
        #If both children are not null
          elif(root.right and root.left):
             sub=self.minNode(root.right)
             root.value=sub.value
             root.right=self.__help_delete(root.right,sub.value)
             return root
          
      #If both children are null
          elif(not root.right and not root.left):
             root=None
             return root
      
      #Traverse through the right subtreee
       elif(root.value< value):
          root.right=self.__help_delete(root.right,value)
          return root 
       
      #Traverse through the left subtree
       elif(root.value> value):
          root.left=self.__help_delete(root.left,value)
          return root    

    
        

test=Tree()
test.insert(3)
test.insert(8)
test.insert(4)

test.delete(8)
print(test.root.right.value)