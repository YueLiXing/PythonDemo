# 976. 三角形的最大周长  显示英文描述
# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
# 如果不能形成任何面积不为零的三角形，返回 0。

# https: // leetcode-cn.com/contest/weekly-contest-119/problems/largest-perimeter-triangle/


import time

class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 三角形，任意两边之和大于第三边，任意两边之差小于第三边
        # startTime = time.time()
        A.sort(reverse=True)
        # print("sort: ",time.time()-startTime)
        result = 0
        for indexA in range(len(A)-2):
            for indexB in range(indexA+1, len(A)-1):
                for indexC in range(indexB+1, len(A)):
                    a = A[indexA]
                    b = A[indexB]
                    c = A[indexC]
                    if a-b > c:
                        break
                    if a-c > b:
                        break
                    # print(a,b,c)
                    if b+c > a and a-b < c and a-c < b:
                        temp = a+b+c
                        if temp > result:
                            return temp
                            # print("temp", temp)
                            # result = temp
        return result

test = Solution()

print(test.largestPerimeter([2,1,2]))
startTime = time.time()
print(test.largestPerimeter([22,96,50,31,27,67,24,99,90,59,49,66,82,12,88,41,53,43,21,58,95,89,8,61,80,9,36,5,68,24,39,61,61,52,57,11,5506,4,10,43,64,34,20,46,85,86,95,19,65,66,3,64,100,80,26,82,95,32,95,72,8,36,54,78,63,10,89,92,42,14,78,64,22,99,59,18,69,56,29,75,60,100,14,6,6,23,56,40,29,81,27,39,6,13,79,100,69,19,94,89,95,63,4,92,74,22,73,84,27,7,3,76,30,35,90,33,74,60,90,69,100,61,98,43,3,95,46,16,9,97,23,35,86,56,49,60,35,44,28,38,2093,26,6,77,78,8,54,87,81,49,12,98,79,13,61,57,73,59,46,82,83,14,81,43,51,88,21,50,30,87,97,35,78,14,38,47,11,1296,74,93,52,75,93,11,75,84,54,5,12,17,49,49,34,98,47,82,93,59,82,678989,70,55,74,70,82,25,39,71,61,33,92,38,65,32,20,46,34,66,36,30,70,59,28,77,81,43,1,79,98,38,56,29,88,80,77,4,55,92,89,32,50,31,72,57,87,12,15,32,59,19,16,73,84,7,55,12,95,8,34,4,89,83,10,20,92,24,29,12,4,20,47,59,23,51,49,96,73,72,43,97,5,60,55,43,99053,7,94,23,40,88,31,10,41,41,61,52,23,59,96,99,9,82,20,15,72,11,26,3,56,62,4,54,2,5,85,80,43,74,1,75,30,48,17,36,70,67,1,62,92,85,73,39,25,42,1,74,69,93,29,12,20,8918,26,78,21,39,1,68,61,37,48,27,97,60,81,26,18,7,49,71,30,8,24,71,78,33,98,67,39,15,2,57,18,6,34,59,68,4,32,50,13,80,88,73,54,6,89,28,69,73,49,5,51,13,41,21,79,59,17,54,6,84,11,17,16,11,27,65,37,69,31,495,1,64,86,24,1,95,69,32,63,10,77,88,20,26,37,93,13,35,100,47,77,62,48,84,5,95,79,46,64,29,17,57,26,34,13,41,11,63,69,33,61,94,21,61,11,34,41,41,75,37,31,21,33,50,96,58,64,82,46,57,419634,6,40,49,69,67,76,98,71,100,42,76,36,47,24,51,28,86,75,25,11,2,54,84,70,40,55,5,47,19,48,37,44,1,17,76,89,37,79,84,62,61,80,85,94,34,34,8,44,54,67,38,46,7,5,38,48,79,38,61,99,100,1,5,36,20,60,96,75,90,26,43,29,62,6,52,39,63,23,93,57,31,3,29,69,74,86,81,40,49,17,90,87,97,82,21,71,95,71,94,45,3,100,82,20,6,94,57,2,20,48,90,259339,66,56,39,87,60,16,45,9,97,97,32,99,35,83,1,15,25,18,96,50,58,11,83,8,1,53,46,18,29,35,42,22,95,9,60,84,14,37,82,14444,10,59,54,5,19,47,53,20,44,31,37,19,74,13,94,27,23,71,82,55,16,21,12,20,63,30,57,87,33,78,80,39,13,71,21,99,53,76,97,98,80,61,77,30,92,69,77,69,31,296,36,61,64,96,17,94,56,22,26,90,73,91,96,71,80,36,72,51,1,8,4,98,43,42,92,72,36,81,19,75,75,71,15,72,31,67,13,58,79,48,89,16,91,31,77,68,16,14,59,89,77,36,27,70,72,76,21,61,24,61,22,44,38,96,37824,29,69,57,77,66,28,10,38,83,6,55,35,27,73,54,66,86,18,65,58,73,100,21,13,794,34,77,32,38,45,36,99,60,24,59,74,63,99,44,29,90,89,53,57,38,70,15,70,84,31,45,41,9,51,95,14,7,48,11,41,11,87,68,92,58,33,66,8,82,38,65,12,52,35,51,3400,92,42,75,82,37,41,66,98,10,56,58,80,53,30,26,43,19,55,83,49,16,39,48,74,27,10,16,5,85,43,70,71,67,1,23369,94,42,39,15,91,92,11,81,85,58,8,43,81,13,74,38,14,8,27,38,55,92,75,33,11,94,38,58,33,90,61,55,33,1,19,96,91,25,89,75,81,20,62,10,44,87,6,76,72,87,48,44,22,18,181,23,75,18,83,47,79,91,75,2,85,57,71,64,11,4,84,70,97,80,51,61211,48,92,25,2,91,87,62,69,82,160275,67,31,97,26,50,65,87,97,35,83,56,44,58,42,17,41,77,83,34,88,26,73,22,65,83,91,14,3,55,100,84,23,46,39,78,39,68,35,100,91,40,56,13,97,94,94,46,3,7,13,18,86,47,39,18,67,94,40,6,70,32,37,21]))
print(time.time()-startTime)
