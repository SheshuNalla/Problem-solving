def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        mini = i
        for j in range(i,n):
            if arr[j] < arr[mini]:
                mini = j

        temp = arr[i]
        arr[i] = arr[mini]
        arr[mini] = temp
    return arr

numbers = list(map(int, input().split()))
print(selection_sort(numbers))