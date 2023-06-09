class Node
{
    constructor(data)
    {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}


export default class BinaryTree{
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

delete(data)
{
    this.root = this.deleteNode(this.root, data);
}
 
deleteNode(node, key)
{
         
    if(node === null)
        return null;
 
    
    else if(key < node.data)
    {
        node.left = this.deleteNode(node.left, key);
        return node;
    }
 
    
    else if(key > node.data)
    {
        node.right = this.deleteNode(node.right, key);
        return node;
    }
 
    else
    {
         if(node.left === null && node.right === null)
        {
            node = null;
            return node;
        }
 
        
        if(node.left === null)
        {
            node = node.right;
            return node;
        }
         
        else if(node.right === null)
        {
            node = node.left;
            return node;
        }
 
       
        let temp = this.MinNode(node.right);
        node.data = temp.data;
 
        node.right = this.deleteNode(node.right, temp.data);
        return node;
    }
 
}

}
let test= new BinaryTree()
test.insert(7)
test.insert(4)
test.insert(9)
test.delete(4)
console.log(test)/*BinaryTree {
    root: Node {
      data: 7,
      left: null,
      right: Node { data: 9, left: null, right: null }
    }*/