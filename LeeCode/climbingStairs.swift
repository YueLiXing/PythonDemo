class Solution {
    func climbStairs(_ n: Int) -> Int {
        var target = 1
        var lastCache0 = 0
        var lastCache1 = 0
        
        for _ in 1...n {
            lastCache1 = lastCache0
            lastCache0 = target
            target = lastCache0+lastCache1
        }
        return target
    }
}