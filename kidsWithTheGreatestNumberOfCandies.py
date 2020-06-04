class Solution:
    def kidsWithCandies(self, candies: [int], extraCandies: int) -> [bool]:
        maxCandy = candies[0]
        for tempC in candies:
            if tempC > maxCandy:
                maxCandy = tempC
        result = []
        for tempC in candies:
            result.append(tempC+extraCandies >= maxCandy)
        return result
