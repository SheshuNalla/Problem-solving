# Optimized code for an array is already in sorted form:

arr = list(map(int, input().split()))
for i in range(len(arr), 0, -1):
    swap = 0
    for j in range(0, i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swap =1
    
    if swap == 0:
        break
    print('runs')
print(arr)