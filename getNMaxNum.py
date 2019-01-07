# -*- coding: utf-8 -*-
# 获取一个数组中第N大的元素
# https://mp.weixin.qq.com/s/LKrxeFT9S5NEAHlhHI3nSQ

import random

#  寻找第k大的元素
#  @param array  待调整的堆
#  @param k  第几大
#
def findNumberK(array,k):
    #  1.用前k个元素构建小顶堆
    buildHeap(array, k)
    # 2.继续遍历数组，和堆顶比较
    for i in range(len(array)):
        if i>=k:
            if array[i] > array[0]:
                array[0] = array[i]
                downAdjust(array,0,k)
        else:
            continue
    # 3.返回堆顶元素
    return array[0]

# 构建堆
# @param array  待调整的堆
# @param length  堆的有效大小
def buildHeap(array,length):
    # 从最后一个非叶子节点开始，依次下沉调整
    for i in range(int((length - 2)/2), -1, -1):
        downAdjust(array, i, length)        

# * 下沉调整
# * @param array     待调整的堆
# * @param index    要下沉的节点
# * @param length    堆的有效大小
def downAdjust(array,index,length):
    # temp保存父节点值，用于最后的赋值
    temp = array[index]
    childIndex = 2*index+1
    while childIndex < length:
        # 如果有右孩子，且右孩子小于左孩子的值，则定位到右孩子
        if childIndex+1 < length and array[childIndex+1]<array[childIndex]:
            childIndex+=1

        # 如果父节点小于任何一个孩子的值，直接跳出
        if temp <= array[childIndex]:
            break

        # 无需真正交换，单向赋值即可
        array[index] = array[childIndex]
        index = childIndex
        childIndex = 2*childIndex+1
    array[index] = temp




# 插入法 取无序数组里的第n大数字
def findNumberK2(array, n):
    minArray = array[0:n]
    minArray.sort(reverse=1)
    
    for index in range(n,len(array)):
        if array[index] > minArray[-1]:
            for minIndex in range(len(minArray)):
                if array[index] > minArray[minIndex]:
                    minArray.insert(minIndex, array[index])
                    break
            minArray.pop()
            print(minArray)
    return minArray[-1]

# 分治法
def findNumberK3(array,n):
    print("start", array)
    centerIndex = 0
    for index in range(0, len(array)):
        if index != centerIndex and array[index] >= array[centerIndex]:
            temp = array.pop(index)
            array.insert(0, temp)
            centerIndex += 1
            print(array)

    if centerIndex+1 == n:
        return array[centerIndex]
    elif centerIndex+1 < n:
        print("裁右边","centerIndex:",centerIndex,"n",n)
        return findNumberK3(array[centerIndex+1:], n-(centerIndex+1))
    else:
        print("裁左边", "centerIndex:", centerIndex, "n", n)
        return findNumberK3(array[:centerIndex], n)



if __name__ == "__main__":
    array = []
    for index in range(0,30):
        array.append(random.randint(0, 100))
        pass
    # array = [7,5,15,3,17,2,20,24,1,9,12,8]
    n = 10
    print(findNumberK(array.copy(), n), "findNumberK")
    print(findNumberK2(array.copy(), n), "findNumberK2")
    print(findNumberK3(array.copy(), n), "findNumberK3")
    
    print(array,"+")
    # 最暴力的方法，直接降序排序，取 n-1
    array.sort(reverse=1)
    print(array)
    print(array[n-1])
