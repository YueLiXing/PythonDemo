class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0:
            if n == 1:
                return True
            else:
                while n >= 2:
                    if n == 2:
                        return True
                    n = n/2
                    if n%2 == 0:
                        continue
                    else:
                        return False
        else:
            return False

print(Solution().isPowerOfTwo(1))
print(Solution().isPowerOfTwo(2))
print(Solution().isPowerOfTwo(3))
print(Solution().isPowerOfTwo(4))
