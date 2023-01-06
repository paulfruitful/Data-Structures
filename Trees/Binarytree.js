class node{
    constructor(root,left,right){
        this.root=root
        this.left=left
        this.right=right
    }
}


class BinaryTree{
  constructor(root){
    this.root=new node(root,null,null)
    this.height=null
  }

  insert(node){
    let current= this.root
    while(true){
       if(current.left==null){
        current=current.left
        current=new node(node,null, null)
        break
       }else if(current.right==null){
        current=current.right
        current.right=new node(node,null, null)
        break   
    }
       
    }}
  }


let test= new BinaryTree(8)
test.insert(7)
console.log(test)