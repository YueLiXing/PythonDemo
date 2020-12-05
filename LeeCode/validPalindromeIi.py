class Solution:
    def validPalindrome(self, s):
        front = 0
        last = len(s)-1
        while front < last:
            if s[front] == s[last]:
                front += 1
                last -= 1
            else:
                return self.valid(s[front+1:last+1]) or self.valid(s[front:last])
        return True

    def valid(self, s):
        print(s)
        front = 0
        last = len(s)-1
        while front < last:
            if s[front] == s[last]:
                front += 1
                last -= 1
            else:
                return False
        return True
        # """
        # :type s: str
        # :rtype: bool
        # """
        # flag = 0
        # l = len(s)
        # front = 0
        # last = l-1
        # while front < last:
        #     if s[front] == s[last]:
        #         front += 1
        #         last -= 1
        #     else:
        #         if flag == 0:
        #             flag = 1
        #             front += 1
        #         else:
        #             flag = 0
        #             front = 0
        #             last = l-1
        #             while front < last:
        #                 # print(s[front],s[last],front,last)
        #                 if s[front] == s[last]:
        #                     front += 1
        #                     last -= 1
        #                 else:
        #                     if flag == 0:
        #                         flag = 1
        #                         last -= 1
        #                     else:
        #                         return False
        
        # return True
            

print(Solution().validPalindrome("abc"))
# print(Solution().validPalindrome("cbbcc"))
