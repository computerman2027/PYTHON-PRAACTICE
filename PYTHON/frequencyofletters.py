st=input("ENter a string : ")

frequency={}

for ch in st:
    if ch in frequency:
        frequency[ch]+=1
    else:
        frequency[ch]=1

print(frequency)

for i in frequency:
    print(f"{i} is present {frequency[i]} times")