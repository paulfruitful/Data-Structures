function node(head,next){
  this.head=head
  this.next=next
}

class linkedList{
    construct(){
       this.head=null
       this.length=0
    }

    insert(element){
    let newNode=node(element,this.head)
    this.length++
    }
}


const test= new linkedList()
test.insert(5)
test.insert(3)
console.log(test)