def findFirstOccurrence(nums, target):
    (left, right) = (0, len(nums) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            result = mid
            right = mid - 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
 
 
nums = [10,10,10,20,20,20,20,40]
target = 20

index = findFirstOccurrence(nums, target)

if index != -1:
    print(index)
else:
    print("-1")