st=input("Enter a sentence : ")
st=st+" "
ans=""
l=len(st)
for i in range(l-1):
    if not(st[i]==" " and st[i+1]==" "):
        ans=ans+st[i]
print(f"Ans = {ans}")