

const {BinaryTree,Node}=require('../Non-Linear Data Structure/Trees/Binarytree')

const test=[4,78,1,-1, 67,6,5]


function binarySearch(arr){
    const node=new BinaryTree();
    arr.forEach(item => {
         node.insert(item)      
    });   

    return node
}


console.log(binarySearch(test))