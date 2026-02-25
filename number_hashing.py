
n=int(input())
arr=[]

for i in range(n):
    arr.append(int(input()))

hash_arr=[0]*100
for i in range(n):
    hash_arr[arr[i]]+=1

q=int(input())
while q>0:
    number=int(input())
    print(hash_arr[number])
    q-=1


