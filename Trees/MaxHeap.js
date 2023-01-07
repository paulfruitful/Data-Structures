class MaxHeap{
    constructor(){
        this.heap=[]
    }
    isRoot(index){
        return index==1
    }
    level(index){
        return index/2 
    }
    parent(data){
        
     
    }
    leftchild(index){
        return (2*index)+1
     }
     
rightchild(index)
{
    (2*index)+2
}
  }
  


let test=new MaxHeap