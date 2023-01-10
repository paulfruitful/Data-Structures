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
    isLeaf(index) {
        return (
            index >= Math.floor(this.values.length / 2) && index <= this.values.length - 1
        )
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
    this.goUp(this.values.length - 1);
}
goUp(index){
    let nowIndex=index
    let parentIndex=this.parent(nowIndex)
   while(nowIndex>0 && this.values[nowIndex]>this.values[parentIndex]){
        this.exchange(this.heap[nowIndex],this.heap[parentIndex])
        nowIndex=parentIndex
        parentIndex=this.parent(nowIndex)
   }
}
getMax(){
  if(this.heap.length<1) return "Empty Heap";
  let max=this.heap[0]
  let least = this.heap.pop()
  this.heap[0]=least
 this.goDown(0)
 return max
}
goDown(index){
if(!this.isLeaf()){
  let leftchild=this.leftchild(index)
  let rightchild=this.rightchild(index)
  let maximum= index
  if(this.heap[leftchild]>this.heap[maximum]){
     maximum=leftchild
  }
}
}

  }
  

