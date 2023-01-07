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

exchange(i1,i2){
    this.values[i1],this.values[i2]=this.values[i2],this.values[i1]
}
add(node) {
    // add element to the end of the heap
    this.values.push(element);
    // move element up until it's in the correct position
    this.Up(this.values.length - 1);
}
Up(index){
    let nowIndex=index
    let parentIndex=this.parent(nowIndex)
    
}
  }
  


let test=new MaxHeap