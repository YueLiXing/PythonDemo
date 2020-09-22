# 一个递增数组，将最后面的几个连续元素移动到前面，使用二分查找元素的索引，不存在则返回 -1
def find(arr: [int], target: int):
    low = 0
    high = len(arr)-1
    flag = False
    while low <= high:
        mid = (low+high)//2
        # print(arr[low], arr[mid], arr[high], target)
        if arr[low] < arr[high]:
            aMid = arr[mid]
            if aMid > target:
                high = mid-1
            elif aMid < target:
                low = mid+1
            else:
                return mid
        else:
            if arr[mid] < target:
                if arr[low] > target:
                    low = mid+1
                elif arr[low] < target:
                    high = mid-1
                else:
                    return low
            elif arr[mid] > target:
                if arr[low] > arr[mid]:
                    high = mid-1
                elif arr[low] < arr[mid]:
                    low = mid+1
            else:
                return mid

    return -1


#print(find([4,5,6,7,8,9,1,2,3], 5))
#print(find([4,5,6,7,8,9,1,2,3], 7))

for temp in [8, 9, 1, 2, 3, 4, 5, 6, 7, 99, -1]:
    # for temp in range(11):
    print("result:", find([8, 9, 1, 2, 3, 4, 5, 6, 7], temp))
# print(find([8, 9, 1, 2, 3, 4, 5, 6, 7], 1))
