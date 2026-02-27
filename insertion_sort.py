def insertion_sort(arr):
    for i in range(len(arr)):
        j=i
        print(j,end=" ")
        while(j>0 and arr[j-1]>arr[j]):
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
        print(j,end=" ")

    return arr

arr=[14,9,15,12,6,8,13]

print(insertion_sort(arr))