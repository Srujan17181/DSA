# Given an integer array nums, move all the 0's to the end of the array. 
# The relative order of the other elements must remain the same.


arr=[0, 1, 4, 0, 5, 2]

j=-1
for i in range(len(arr)-1):
    if arr[i]==0:
        j=i
        break


for i in range(j+1,len(arr)):
    if arr[i]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        j+=1

        

print(arr)





# for i in range(len(arr)-1):
#     if arr[i]==0:
#         j=arr[i]
#         arr[i]=arr[i+1]
#         arr[i+1]=j

# print(arr)