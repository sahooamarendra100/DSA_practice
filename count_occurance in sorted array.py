def findLastOccurrence(nums, target):
 
    (left, right) = (0, len(nums) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            result = mid
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
    
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
 
 
if __name__ == '__main__':
 
    nums = [10,10,10,10,20,20,40]
    target = 10
 
    index = findLastOccurrence(nums, target)
    index_1 = findFirstOccurrence(nums, target)
    length = index - index_1 +1
    print(length)