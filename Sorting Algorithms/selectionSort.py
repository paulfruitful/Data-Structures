def selectionSort(a):
        for  i in range(0,len(a)):
            k=i
            for j in range(1,len(a)):
                  if a[j]>a[k]:
                        k=j
                  else:
                        k=k
            
            a[k],a[i]=a[i],a[k]     
        return a

array=[6,8,3,2,1,20,14,35,67,23,7]

selectionSort(array)

print(array)
