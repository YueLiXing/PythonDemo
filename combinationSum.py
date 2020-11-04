class Solution:
    def combinationSum(self, candidates: [int], target: int):
        result = []
        self._comSum(sorted(candidates), 0, target, [], result)
        return result

    def _comSum(self, candidates: [int], index: int, target: int, cobine: [int], result: [[int]]):
        if target == 0:
            result.append(cobine)
            return
        if index >= len(candidates):
            return
        current = candidates[index]
        if current <= target:
            self._comSum(candidates, index+1, target, cobine, result)
            temp = cobine.copy()
            temp.append(current)
            self._comSum(candidates, index, target-current, temp, result)


print(Solution().combinationSum([2, 3, 6, 7], 7))
print(Solution().combinationSum([2, 3, 5], 8))
