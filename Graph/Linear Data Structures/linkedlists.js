class  node{
    constructor(head,next){ 
  this.head=head
  this.next=next
}
}

class linkedList{
    construct(){
       this.head=null
       this.size=null
    }

    insert(element){
    let newNode=new node(element,this.head) 
    this.head=newNode
    this.size++
    }
}


const test= new linkedList()
test.insert(5)
test.insert(6)
test.insert(3)
console.log(test)