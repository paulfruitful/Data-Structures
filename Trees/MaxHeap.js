class Node{
    constructor(data){
        this.data=data
        this.left=null
        this.right=null
    }
    delete(){
        this.data=this.left
    }
}

class MaxHeap{
    constructor(){
        this.root=null
    }
    insertroot(data){
        let node= new Node(data)
        if(this.root==null){
        this.root=node
        }else{
            return "There's an existing root"
        }
     
    }
    insertLeft(Newnode){
        let newnode=new Node(Newnode)
       if(this.root<newnode.data){
           return console.log('The Node to be inserted is greater than root node')
       }else{
          if(this.root.left==null){
            this.root.left=newnode
          }else if(this.root.left.data<newnode){
            return console.log('The Node to be inserted is greater than root node')
          }else{
            this.insertNode(this.root.left,newnode)
          }
       }
     }
     
insertNode(node, newNode)
{
    if(newNode.data > node.right)
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
  


let test=new MaxHeap
test.insertroot(20)
test.insertLeft(5)
test.insertLeft(4)
test.insertLeft(3)
test.insertLeft(2)
console.log(test)