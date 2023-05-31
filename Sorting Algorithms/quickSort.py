def choosePivot(a):
   pivot=(len(a)-1)/2
   return pivot
def partition(a, l,r):
   pivotIndex=choosePivot(a)
   pivot=a[pivotIndex]
   leftmark=l
   rightmark=r-1
   a[pivotIndex],a[r]=a[r],a[pivotIndex]
   while(leftmark<=rightmark):
      while(leftmark<=rightmark and leftmark<=pivot):
         leftmark+=1
      while(leftmark<=rightmark and rightmark>=pivot):
         rightmark-=1
      if (leftmark<rightmark):
         a[rightmark],a[leftmark]=a[leftmark],a[rightmark]
   a[leftmark],a[r]=a[r],a[leftmark]
   return leftmark



def quicksort(arr, left,right):
   while(left<right):
      pivot=partition(arr,left,right)
      quicksort(arr,pivot+1,right)
      quicksort(arr,left,pivot-1)