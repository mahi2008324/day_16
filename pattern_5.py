for i in range(10):
    for j in range(10):
        if i+j==5 or i-j==5:
            print("<",end=" ")
        else:
            print(" ",end=" ")
    print()