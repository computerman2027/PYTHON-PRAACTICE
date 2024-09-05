st="imon Mallik|28-9-2004|06-9-2030"

st1=st.split("|")
st2=st1[1].split('-')
st3=st1[2].split('-')
age=int(st3[2])-int(st2[2])
print("Age = {0}".format(age))