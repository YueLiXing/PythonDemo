/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */
class Solution {
    func levelOrder(_ root: TreeNode?) -> [[Int]] {
        var result = [[Int]]()
        if root != nil {
            var cacheArr = [[TreeNode]]()
            cacheArr.append([root!])
            var level = 0
            while cacheArr.count > 0 {
                var tempArr = [TreeNode]()
                if level == result.count {
                    result.append([])
                }
                for tempNode in cacheArr[0] {
                    result[level].append(tempNode.val)
                    if tempNode.left != nil {
                        tempArr.append(tempNode.left!)
                    }
                    if tempNode.right != nil {
                        tempArr.append(tempNode.right!)
                    }
                }
                if tempArr.count > 0 {
                    cacheArr.append(tempArr)
                }
                level += 1
                cacheArr.remove(at: 0)
            }
        }
        return result
    }
}