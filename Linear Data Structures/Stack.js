class Stack{
 constructor(){
   let stack=[]
   let length=0

 }
 
push(value){
this.stack.push(value)
this.length++

 }

 pull(){
    this.stack.pop()
    this.length--
     }
}


let Test=new Stack()
Test.push(34)
Test.push(45)
Test.push(23)

console.log(Test)