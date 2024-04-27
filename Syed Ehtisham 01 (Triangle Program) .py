#increasing Trinangle assignment program
val = int(input("Enter the height of the triangle: "))
for i in range(val):
    for j in range(1+i):
        if(i%2==0):
            print("*", end = "")
        else:
            print("#", end = "")
    print()
    

#decresing Triangle assignment program
val = int(input("Enter the height of the triangle: "))
for i in range(val):
    for j in range(i,val):
        if(i%2==0):
            print("&", end = "")
        else:
            print("@", end = "")
    print()
    
#increment triangle with condition assignment program
val = int(input("Enter the height of the triangle: "))
for i in range(val):
    for j in range(1+i):
        print(i+1,end=" ")
    print()
    

#decrement triangle with condition assignment program
val = int(input("Enter the height of the triangle: "))
for i in range(val):
    for j in range(i,val):
        print(i,end=" ")
    print()
    
    