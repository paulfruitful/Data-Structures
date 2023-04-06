def insertSort(array):

    for i in range(1, len(array)):
      current=array[i]
      prev=i-1
      while prev>=0 and array[prev] >current:
         array[i+1]= array[prev]
         prev-=1
      array[prev+1]=current
    return array

def insertSort_dec(array):

    for i in range(1, len(array)):
      current=array[i]
      prev=i-1
      while prev>=0 and array[prev] <current:
         array[i+1]= array[prev]
         prev-=1
      array[prev+1]=current
    return array


a=[6,8,3,2,1,20,14,35,67,23,7]

insertSort(a)
print(a)