n = int(input())
for i in range( n):
        #space
        for j in range(n-i-1):
            print(" ", end="")
        #stars
        for j in range(2*i+1):
            print("*", end="")
        print()
for i in range(1,n):
    #space
    for j in range(i):
        print(" ", end="")
    #stars
    for j in range((2*n)-(2*i)-1):
        print("*", end="")
    #space
    
    print()