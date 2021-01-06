class Solution {
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        var result = [[Int]]()
        let cans = candidates.sorted()
        _combinationSum(cans, target, index: 0, combine: [], result: &result)
        return result
    }
    func _combinationSum(_ candidates: [Int], _ target: Int, index: Int, combine:[Int], result: inout [[Int]]) {
        if target == 0 {
            result.append(combine)
            return
        }
        if index >= candidates.count {
            return
        }
        let current = candidates[index]
        if current <= target {
            _combinationSum(candidates, target, index: index+1, combine: combine, result: &result)
            var c = combine
            c.append(current)
            _combinationSum(candidates, target-current, index: index, combine: c, result: &result)
        }
    }
}