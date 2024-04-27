#increment assignment program
def inc(value):
    for i in range(1,value+1):
        for j in range(0,i):
            print(j+1 ,end= "")
        print()
value = int(input("Enter heighest number of triangle, you want: "))
inc(value)

#decrement assignment program
def dec(value):
    for i in range(value , 0 , -1):
        for j in range(i):
            print(j+1 ,end= "")
        print()
value = int(input("Enter heighest number of triangle, you want: "))
dec(value)


#increment With condition assignment program
def inc(value):
    for i in range(1,value+1):
        for j in range(0,i):
            if(i%2==0):
                print("+" ,end= "")
            else:
                print("*" ,end= "")
        print()
value = int(input("Enter heighest number of triangle, you want: "))
inc(value)

#decrement assignment program
def dec(value):
    for i in range(value , 0 , -1):
        for j in range(i):
            if(i%2==0):
                print("#" ,end= "")
            else:
                print("&" ,end= "")
        print()
value = int(input("Enter heighest number of triangle, you want: "))
dec(value)