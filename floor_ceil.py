arr=[3, 4, 4, 7, 8, 10]

def floor_(arr,target):
    n=len(arr)
    low=0
    high=n-1
    floor=-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]<=target:
            floor=arr[mid]
            low=mid+1
            
        else:
            high=mid-1
    return floor


def ceil_(arr,target):
    n=len(arr)
    low=0
    high=n-1
    ceil=-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>=target:
            ceil=arr[mid]
            high=mid-1
            
        else:
            low=mid+1
    return ceil
print([floor_(arr,5),ceil_(arr,5)])