arr=[3,1,2]

def subsequence(ind,list):
    global arr
    if (ind>=len(arr)):
        print(list)
        return
    list.append(arr[ind])
    subsequence(ind+1,list)
    list.remove(arr[ind])
    subsequence(ind+1,list)


subsequence(0,[])