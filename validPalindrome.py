class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        front = 0
        last = len(s)-1
        while front < last:
            tempFC = s[front]
            tempLC = s[last]
            if ("a" <= tempFC <= "z" or "A" <= tempFC <= "Z" or "0" <= tempFC <= "9") == False:
                front += 1
                continue
            if ("a" <= tempLC <= "z" or "A" <= tempLC <= "Z" or "0" <= tempLC <= "9") == False:
                last -= 1
                continue
            if tempFC.lower() == tempLC.lower():
                front += 1
                last -= 1
            else:
                return False
        return True


        # target = ""
        # for tempC in s:
        #     if "a"<=tempC<="z" or "A"<=tempC<="Z" or "0"<=tempC<="9":
        #         target += tempC.lower()
        # front = 0
        # last = len(target)-1
        # while front < last:
        #     if target[front] == target[last]:
        #         front += 1
        #         last -= 1
        #     else:
        #         return False
        # return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("OP"))
