def TwoSum(nums, target):
    seen = {}
    for i,num in enumerate(nums):
        required = target - num
        if required in seen:
            return [seen[required], i]
        else:
            seen[num] = i

nums = list(map(int, input().split()))
target = int(input())

print(TwoSum(nums, target))