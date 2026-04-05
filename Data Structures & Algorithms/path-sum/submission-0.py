# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, targetSum, currentSum):
            if not root:
                return False
                
            if root.left == None and root.right == None:
                return targetSum == currentSum + root.val
            return dfs(root.left, targetSum, currentSum + root.val) or dfs(root.right, targetSum, currentSum + root.val)
        return dfs(root, targetSum, 0)