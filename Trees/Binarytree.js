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
    if(current==null){
        current=new node(node,null, null)
        break
    }else{
       if(current.left==null){
        current.left=new node(node,null, null)
        break
       }else if(){
        
       }
       
    }}
  }
}