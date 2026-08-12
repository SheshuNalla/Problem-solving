def mS(arr):
    if len(arr)>1:
        # find middle
        mid = len(arr)//2
        
        #Divide Array
        left = arr[ :mid]
        right = arr[mid: ]

        #Recursively sort both halves
        mS(left)
        mS(right)

        i=j=k = 0

        # Merge two sorted arrays
        while i < len(left) and j <len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j+=1
            k +=1

        # Copy remaining elements from left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements from right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = list(map(int, input().split()))
mS(arr)
print(arr)
        



