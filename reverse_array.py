name="madam"

def reverse(i,n):
    global name
    if (i>=(len(name)//2)):
        return True
    elif (name[i]!=name[len(name)-i-1]):
        return False
    
    else:
        reverse(i+1,n)

print(reverse(0,5))
