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
      self.help_insert(data,self.root)


    def help_insert(self,data,root):
        if not root:
            root=Node(data)
            return 
        elif root.value>data:
            self.help_insert(data,root.right)
        elif root.value<data:
            self.help_insert(data,root.left)
        

test=Tree()
test.insert(3)

test.insert(8)
print(test.root)