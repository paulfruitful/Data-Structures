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
}