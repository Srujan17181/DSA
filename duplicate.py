arr=[1,2,3,1]
def contain_duplicate(nums):
    hashset=set()

    for n in arr:
        if n in hashset:
            return True
        
        hashset.add(n)
        return False
    

print(contain_duplicate(arr))