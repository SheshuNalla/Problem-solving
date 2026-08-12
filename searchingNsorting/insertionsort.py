arr = list(map(int, input().split()))

for i in range(0,len(arr)):
    j = i
    while j > 0 and arr[j-1] > arr[j]:
        temp = arr[j]
        arr[j] =arr[j-1]
        arr[j-1] = temp
        j -= 1
        print("runs")
print(arr)