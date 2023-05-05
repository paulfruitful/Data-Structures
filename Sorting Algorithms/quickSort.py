def quicksort(arr, left,right):
   while(left<right):
      pivot=partition(arr,left,right)
      quicksort(arr,pivot+1,right)
      quicksort(arr,left,pivot-1)
