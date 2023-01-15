class Node
{
    constructor(data)
    {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}


class BinaryTree{
  constructor(root){
    this.root=null
 
  }


insert(data)
{
    
    let newNode = new Node(data);

    if(this.root === null)
        this.root = newNode;
    else
 
        this.insertNode(this.root, newNode);
}
insertNode(node, newNode)
{
    if(newNode.data < node.data)
    {
        if(node.left === null)
            node.left = newNode;
        else
 
         
            this.insertNode(node.left, newNode);
    }
 
    else
    {
        if(node.right === null)
            node.right = newNode;
        else
 
            
            this.insertNode(node.right,newNode);
    }
}

MinNode(node)
{
   
    if(node.left === null)
        return node;
    else
        return this.MinNode(node.left);
}

}
let test= new BinaryTree()
test.insert(7)
test.insert(4)
test.insert(9)
console.log(test)/*  root: Node {
    data: 7,
    left: Node { data: 4, left: null, right: null },
    right: Node { data: 9, left: null, right: null }
  }
}*/