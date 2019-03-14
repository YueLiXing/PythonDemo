class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        valueDict = {
             1 : "I",
             5 : "V",
             10 : "X",
             50 : "L",
             100 : "C",
             500 : "D",
             1000 : "M"
        }
        keyArr = [1000,500,100,50,10,5,1]
        #           0   1   2   3  4 5 6
        #           2   2   4   4  6 6
        indexK = 0
        target = ""
        while num > 0 and indexK < len(keyArr):
            temp = keyArr[indexK]
            if num // keyArr[indexK] > 0:
                
                count = num // temp
                for i in range(count):
                    target += valueDict[temp]
                num -= temp*count
                # print("1, ", num)
            
            if indexK+2-indexK%2 < len(keyArr):
                temp1 = keyArr[indexK+2-indexK % 2]
                # print(num, keyArr[indexK]-temp1)
                if num >= keyArr[indexK]-temp1:
                    target += valueDict[temp1]+valueDict[temp]
                    num -= keyArr[indexK]-temp1
                    # print("2, ", num)

            indexK += 1
        return target


print(Solution().intToRoman(1900))
print(Solution().intToRoman(40))
print(Solution().intToRoman(9))
print(Solution().intToRoman(4))
