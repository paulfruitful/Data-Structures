def choosePivot(a):
   pivot=(len(a)-1)/2
   return pivot
def partition(a, l,r):
   pivot=choosePivot(a)
   leftmark=l+1
   return leftmark



def quicksort(arr, left,right):
   while(left<right):
      pivot=0