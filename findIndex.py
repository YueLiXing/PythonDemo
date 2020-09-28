# 一个递增数组，将最后面的几个连续元素移动到前面，使用二分查找元素的索引，不存在则返回 -1
def find(arr: [int], target: int):
    low = 0
    high = len(arr)-1
    flag = False
    while low <= high:
        mid = (low+high)//2+(low+high) % 2
        # print(arr[low], arr[mid], arr[high], target)
        if arr[mid] == target:
            return mid
        if arr[low] < arr[mid]:
            if arr[low] <= target <= arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid] <= target <= arr[high]:
                low = mid+1
            else:
                high = mid-1
        # if arr[low] < arr[high]:
        #     aMid = arr[mid]
        #     if aMid > target:
        #         high = mid-1
        #     elif aMid < target:
        #         low = mid+1
        #     else:
        #         return mid
        # else:
        #     if arr[mid] < target:
        #         if arr[low] > target:
        #             low = mid+1
        #         else:
        #             if arr[mid] > arr[low]:
        #                 low = mid+1
        #             else:
        #                 high = mid-1
        #     elif arr[mid] > target:
        #         if arr[low] > target:
        #             if arr[low] > a[mid]:
        #                 high = mid-1
        #             else:
        #                 low = mid+1
        #         else:
        #             high = mid-1

        #     else:
        #         return mid

    return -1


#print(find([4,5,6,7,8,9,1,2,3], 5))
#print(find([4,5,6,7,8,9,1,2,3], 7))

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for k in range(1, len(a)):
    t = a[len(a)-k:len(a)]+a[:len(a)-k]
    print(t)
    for temp in t+[99, -1]:
        print("result:", temp, find(t, temp),
              t.index(temp) if temp in t else -1)

# a = [8, 9, 1, 2, 3, 4, 5, 6, 7]
# for temp in a+[99, -1]:
#     print("result:", find(a, temp), a.index(temp) if temp in a else -1)
# a = [4, 5, 6, 7, 8, 9, 1, 2, 3]
# for temp in a+[99, -1]:
#     print("result:", find(a, temp), a.index(temp) if temp in a else -1)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for temp in a+[99, -1]:
    print("result:", temp, find(t, temp), t.index(temp) if temp in t else -1)
