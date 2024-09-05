name=input("Enter your name : ")
name=name.strip()
namel=name.split(" ")

l=len(namel)
ans=""
for i in range(l-1):
    ans=ans+namel[i][0].capitalize()+"."
ans=ans+namel[l-1].capitalize()
print(f"Initials = {ans}")