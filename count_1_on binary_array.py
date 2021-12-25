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
 
    nums = [0,0,1,1,1,1]
    target = 1
    index_1 = findFirstOccurrence(nums, target)
    count_1 =len(nums)-index_1
    print(count_1)