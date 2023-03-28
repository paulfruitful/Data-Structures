'''
Dynamic Window: Finding the Max Repeating SubString of K length of a String
'''

def findMaxRepeatSubString(string,k):
    maxString=float('inf')
    add=0
    start=0
    subString=set()
    currentString=''
    for i in range(len(string)):
       currentString+=string[i]
       if (i-start)==k-1:
           if currentString in subString:
               subString.pop(currentString)
               maxString=max(maxString,add+1)
           else:
               subString.add(currentString)
               start+=1
    return maxString


test='AAAAAAAAAAAAAAAAAAABBBCCIMMSMSSIIIIIIIAAAAAAAAAIIDNNDNNAAAAAAAAAAHDDDHJAAAAAAAAAAAA'
print(findMaxRepeatSubString(test,5))