def maxSub(arr):
    maxGlobal=arr[0]
    current=maxGlobal
    for i in range(1,len(arr)):
        current=max(current,current+arr[i])
        if current>maxGlobal:
            maxGlobal=current
    return maxGlobal




a=[-1,3,0,7,-14.1,-100,14]
print(maxSub(a))