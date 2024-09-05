total=count=avg=n=0
while True:
    try:
        st=input("Enter number : ")
        if(st=="done"):
            print("total = ",total)
            print("count = ",count)
            print("average = ",round(avg,2))
            break
        else:
            n=int(st)
    except:
        print("Error : Only integer number accepted. Type \"done\" for exit")
    else:
        total+=n
        count+=1
        avg=total/count


#wap which repeatedly readsnumbers until the user enters "done". Once "done" is entered, print out the total, count and average of the numbers. If the user enters anything other than a number detect their mistake using try and except and print an error message and skip to the next number