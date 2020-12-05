class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        count = 0
        while X != Y:
            if X > Y:
                count += X-Y
                X = Y
            elif Y%2 == 0:
                Y = Y//2
                count += 1
            else:
                Y += 1
                count += 1 
        return count

# print(Solution().brokenCalc(5,8))
# print(Solution().brokenCalc(1024,1))
print(Solution().brokenCalc(1, 1000000000))

