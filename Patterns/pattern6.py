n = int(input("Enter a number:"))
for i in range(1,n+2):
    for j in range(1,n-i+2):
        print(j, end=" ")
    print()
