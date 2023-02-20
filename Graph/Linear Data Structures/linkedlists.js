class  node{
    constructor(head,next){ 
  this.head=head
  this.next=next
}
}

class linkedList{
    construct(){
       this.head=null
       this.size=0
    }

    insert(element){
    let newNode=new node(element,this.head)
    this.head=newNode
    this.size=+1
    }
}


const test= new linkedList()
test.insert(5)
test.insert(3)
console.log(test)