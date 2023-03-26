class Graph{
    constructor(){
        this.nodes={}
    }
    addNode(Newnode){
            this.nodes[Newnode]=[]    
    }
    addEdge(node1,node2){
        if(!this.nodes[node1] || !this.nodes[node2]) return "nodes don't exist";
        this.nodes[node1].push(node2)
        this.nodes[node2].push(node1)
        return "Edge between nodes have been connected";
    }
}
  


let test= new Graph()
test.addNode("FirstNode")
test.addNode("SecondNode")
test.addEdge("SecondNode","FirstNode")
console.log(test)
/*Graph {
    nodes: { FirstNode: [ 'SecondNode' ], SecondNode: [ 'FirstNode' ] }
  }*/