
s=["I","V","X","L","C","D","M"]

hash_t=[1,5,10,50,100,500,1000]

STOR={}

for i in range(len(s)):
    STOR[s[i]]=hash_t[i]

s="IV"
result=0
for i in range(len(s)):
    if (i+1< len(s) and STOR[s[i]]<STOR[s[i+1]]):
        result-=STOR[s[i]]
    else:
        result+=STOR[s[i]]

print(result)