class Btree{
 constructor(){
    this.root={}
 }
 insertNode(node){
    if (this.root.length==null){
        this.root[node]={}
    }else if(this.root.length<3 && !node in this.root){
        this.root[node]={}
    }else{

    }
 }
}



let test= new Btree()

test.insertNode(5)
test.insertNode(6)
test.insertNode(5)

console.log(test)
