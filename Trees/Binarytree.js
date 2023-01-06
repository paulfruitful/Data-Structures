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
 
  insertNode(node){
    if(this.root.left==null){
        this.root.left=new node(node,null, null)
    }else{
         this.root.right=new node(node,null, null)
    }
  }
}