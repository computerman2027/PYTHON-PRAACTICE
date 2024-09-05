n = int(input("Enter a number : "))

for i in range(1,n):
    print("i = "+str(i))
    if i==n-1:
        break#if break include any time in the program it will not goto to else statement
else:
    print("I am here in else block")