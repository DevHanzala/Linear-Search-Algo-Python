def linera_search(a,key,size):
    flag=0
    for i in range(size):
        if (a[i]==key):
            flag=1
            pos=i+1
            break
    if flag==1:
        print("Number found at:",pos, "Position")
    else:
        print("Number not found")


#main
a=[]
size=int(input("Entre size of list:"))
for i in range(size):
    val=int(input("Entre a number"))
    a.append(val)
key=int(input("Entre a number to search"))   
linera_search(a,size,key)