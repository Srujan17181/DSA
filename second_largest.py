
#better way 
arr=[3,6,12,9,2,1]

largest=arr[0]

for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]

second_largest=arr[0]
for i in range(len(arr)-1):
    if arr[i]>second_largest and arr[i]!=largest:
        second_largest=arr[i]

print(largest,second_largest)
# time complexity is O(2n) = n+n


#optimal code 

largest=arr[0]
Slargest=-1

for i in range(1,len(arr)):
    if arr[i]>largest:
        Slargest=largest
        largest=arr[i]

    elif arr[i]<largest and arr[i]>Slargest:
        Slargest=arr[i]

        
print(largest,Slargest)
        


