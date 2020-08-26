class Solution:
    def threeConsecutiveOdds(self, arr: [int]) -> bool:
        countA = len(arr)
        for index in range(countA-2):
            if arr[index] % 2 == 1 and arr[index+1] % 2 == 1 and arr[index+2] % 2 == 1:
                return True
        return False