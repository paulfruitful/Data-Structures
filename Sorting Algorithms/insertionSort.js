function insertSort(arr){
  
    for(i=1; i<arr.length; i++){
      const current=arr[i]
      let previous=i-1

      while (previous>=0 && arr[previous]>current){
        arr[previous+1]=arr[previous]
        previous-=1
      } 

      arr[previous+1]=current

    }
   


}

let array=[9,3,4,33,13,1,70,-10]
insertSort(array)
console.log(array)