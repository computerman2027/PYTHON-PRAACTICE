name=input("Enter your name : ").strip()
name = " "+name
initial=""
i=0
while(i<len(name)):
    if name[i]==" ":
        initial=initial+name[i+1].upper()+"."
    i+=1
print("Initials = "+initial)