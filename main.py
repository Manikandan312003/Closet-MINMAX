def minmax(arr):
    min,max=arr[0],arr[0]
    for i in arr[1:]:
        if i<min:
            min=i
        if i>max:
            max=i
    return min,max

def closestMinMaxFinder(arr):
    min,max=minmax(arr)
    minin,maxin=-1,-1
    res,closest=len(arr),arr
    for i in range(len(arr)):
        if arr[i]==min:
            minin=i
            if maxin>=0:
                if i-maxin+1<res:
                    res=i-maxin+1
                    closest=arr[i:maxin+1]
        if arr[i]==max:
            maxin=i
            if minin>=0:
                if i-minin+1<res:
                    res=i-minin+1
                    closest=arr[minin:i+1]
    return closest,res
arr=list(map(int,input().split()))
print(closestMinMaxFinder(arr))