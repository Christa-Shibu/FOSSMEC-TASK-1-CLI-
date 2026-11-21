name=input("enter name")
m1=int(input("enter mark"))
m2=int(input("enter mark"))
m3=int(input("enter mark"))
avg=(m1+m2+m3)/3
if avg>=90:
    print(name,"got","A")
elif avg<=80:
    print(name,"got","B")
else:
    print(name,"got","C")

