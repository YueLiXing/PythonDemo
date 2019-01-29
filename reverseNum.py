class Solution:
    def reverse(self, x):
        if not -2147483648 < x < 2147483647:
            return 0
        result = 0
        flag = -1 if x < 0 else 1
        x = abs(x)
        while True:
            if x > 0:
                result *= 10
                result += x % 10
                x /= 10
                x = int(x)
            else:
                break
        result *= flag
        # print(-2147483648 < result < 2147483647, result)
            
        if -2147483648 < result < 2147483647:
            return result
        return 0


# 2147483647
# 9646324351
test = Solution()
# print(test.reverse(123)) # 321
# print(test.reverse(-123))  # -321
# print(test.reverse(120)) # 21
print(test.reverse(9646324351))  # 21



# 求斐波那契数列
# bufferSet = {1:1,2:1}
# def fib(n):
#     global bufferSet
#     if n in bufferSet:
#         return bufferSet[n]
#     else:
#         temp = fib(n-1)+fib(n-2)
#         bufferSet[n] = temp
#         return temp

# import time
# startTime = time.time()
# print(fib(30))
# print("30", time.time()-startTime,"s")
# print(fib(40))
# print("40", time.time()-startTime, "s")
# print(fib(50))
# print("50",time.time()-startTime,"s")
# print(fib(100))
# print("100", time.time()-startTime, "s")
# print(bufferSet)
