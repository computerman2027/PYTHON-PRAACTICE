try:
    st=input("Enter a string : ")
    nst=st[::-1]
    if st==nst:
        print("PALINDROME STRING")
    else:
        print("Non palindrome string")
except:
    print("Error occured")