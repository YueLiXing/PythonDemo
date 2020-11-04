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
    func isSubStructure(_ A: TreeNode?, _ B: TreeNode?) -> Bool {
        if A == nil && B == nil {
            return true
        }
        if A == nil || B == nil {
            return false
        }
        if A?.val == B?.val {
            if _judge(A, B) {
                return true
            }
        }
        return isSubStructure(A?.left, B) || isSubStructure(A?.right, B)
    }
    func _judge(_ A: TreeNode?, _ B: TreeNode?) -> Bool {
        if B == nil {
            return true
        }
        if A == nil {
            return false
        }
        if A?.val == B?.val {
            return _judge(A?.left, B?.left) && _judge(A?.right, B?.right)
        }
        return false
    }
}