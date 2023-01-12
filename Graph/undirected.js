class Graph{
    constructor(){
        this.nodes={}
    }
    addNode(Newnode){
            this.nodes[Newnode]=[]    
    }
    addEdge(node1,node2){
        if(!node1 || !node2) return "nodes don't exist";
    }
}
  


let test= new Graph()
test.addNode("FirstNode")
console.log(test)