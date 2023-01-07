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
    insert(data){
        let node= new Node(data)
        if(this.root==null){
        this.root=node
        }else{
            insertNode(root,node)
        }
        
    }
}