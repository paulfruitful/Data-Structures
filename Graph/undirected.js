class Graph{
    constructor(){
        this.nodes={}
    }
    addNode(Newnode){
            this.nodes[Newnode]=[]    
    }
}
  


let test= new Graph()
test.addNode("FirstNode")
console.log(test)