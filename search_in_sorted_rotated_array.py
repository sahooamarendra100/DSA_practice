def search (arr, l, h, key):
    if l > h:
        return -1
    mid = (l + h) // 2
    if arr[mid] == key:
        return mid
    if arr[l] <= arr[mid]:
        if key >= arr[l] and key <= arr[mid]:
            return search(arr, l, mid-1, key)
        return search(arr, mid + 1, h, key)
    if key >= arr[mid] and key <= arr[h]:
        return search(arr, mid + 1, h, key)
    return search(arr, l, mid-1, key)
 

arr = [10,20,30,40,50,8,9]
key = 8
i = search(arr, 0, len(arr)-1, key)
# if i != -1:
#     print (i)
# else:
#     print (i)
print(i)