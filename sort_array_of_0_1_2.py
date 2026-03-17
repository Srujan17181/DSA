def sort_array_of_0_1_2(arr):
    low=0
    mid=0
    high=len(arr)-1
    for i in range(high):
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            mid+=1
            low+=1
        elif arr[mid]==1:
            mid+=1
        elif arr[mid]==2:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1


    return arr

print(sort_array_of_0_1_2([1,0,2,1,0]))
