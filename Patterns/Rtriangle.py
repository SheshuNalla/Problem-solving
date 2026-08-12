n = int(input("Enter a number:"))
for i in range(1,n+2):
    for j in range(1,i):
        #printing stars(*)
        # print("*", end=' ')

        #printing col increment numbers:
        print(j, end=" ")
    print()