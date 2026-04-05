# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder: left, curr, right
        sol = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            sol.append(root.val)
            dfs(root.right)
        dfs(root)
        return sol