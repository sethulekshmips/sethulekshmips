def idmat(size):
    for i in range(0,size):
        for j in range(0,size):
            if(i==j):
                print("1", end=" ")
            else:
                print("0",end=" ")
        print()
s=int(input("enter the size:"))
print("identitymatrix:")
idmat(s)