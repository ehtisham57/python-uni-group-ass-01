#increment assignment program
def inc(val):
    for i in range(1, val +1):
        print("Z " * i)
inc(9)

#decrement assignment program
def dec(val):
    for i in range(val, 0, -1):
        print("S " * i)
dec(9)