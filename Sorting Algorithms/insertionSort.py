def insertSort(array):

    for i in range(1, len(array)):
      current=array[i]
      prev=i-1 //8
      while prev>=0 and array[prev] >current:
         array[prev+1]= array[prev]
         prev-=1 //-1
      array[prev+1]=current
    return array



a=[8,6]

insertSort(a)
print(a)