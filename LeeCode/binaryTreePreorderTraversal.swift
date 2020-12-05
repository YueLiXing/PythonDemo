/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func preorderTraversal(_ root: TreeNode?) -> [Int] {
        var arr = [Int]()
        preTraversal(root, array: &arr)
        return arr
    }
    func preTraversal(_ root: TreeNode?, array: inout [Int]) {
        guard root != nil else {
            return
        }
        array.append(root!.val)
        preTraversal(root?.left, array: &array)
        preTraversal(root?.right, array: &array)
    }
}