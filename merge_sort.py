# merge sort


def merge(arr,low,high,mid):
    temp=[]
    left=low
    right=mid+1

    while(left<=mid and right<=high):
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
        
    while(left<=mid):
        temp.append(arr[left])
        left+=1
    
    while(right<=high):
        temp.append(arr[right])
        right+=1

    for i in range(low,high):
        arr[i]=temp[i-low]

    return arr


def mergesort(arr,low,high):
    if low>=high:
        return
    
    mid=(low+high)//2
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    merge(arr,low,high,mid)
    
    return arr


arr=[2,1,4,6,5,9,7,13]
print(mergesort(arr,0,7))

