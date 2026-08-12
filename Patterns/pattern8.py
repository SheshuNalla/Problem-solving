n = int(input("Enter a number:"))
for i in range(1,n+1):
    #space
    for j in range(i):
        print(" ", end=" ")
    #stars
    for j in range((2*n)-(2*i)+1):
        print("*", end=" ")
    #space
    
    print()