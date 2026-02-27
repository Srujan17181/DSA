def bubble_sort(arr):
    d=0
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                d=1
        if (d==0):
            break
        print("runs")
    return arr

buubble=bubble_sort([1,2,3,4,5,6])
print(buubble)