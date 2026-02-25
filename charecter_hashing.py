s=input()
# pre store

hash_s=[0]*256
for i in range(len(s)):
    hash_s[ord(s[i])]+=1

# fetch

q=int(input())
while q>0:
    char=input()
    print(hash_s[ord(char)])
    q-=1