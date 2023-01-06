class Node{
    constructor(root,left,right){
        this.root=root
        this.left=left
        this.right=right
    }
}


class BinaryTree{
  constructor(root){
    this.root=null
    this.height=null
  }

  
insert(data)
{
    // 
    var newNode = new Node(data,null,null);
    
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
  }


let test= new BinaryTree(8)
test.insert(7)
test.insert(9)
console.log(test)