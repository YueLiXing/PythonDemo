class Solution {
    func reverse(_ x: Int) -> Int {
        // -2147483647 2147483648
        var tempX = x
        let flag = x > 0 ? 1: -1
        var result = 0
        tempX = abs(tempX)
        while tempX != 0 {
            let t = tempX % 10
            result = result*10+t
            tempX = tempX/10
        }
        result = result*flag
        if -2147483647 <= result & & result <= 2147483648 {
            return result
        }
        return 0
    }
}
