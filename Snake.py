N =int(input("Enter A Number:"))
while N >0:
    if N %2 == 1:
        print("*",end='')
        N -=1
    else:
        print("#",end='')
        N-=1
    