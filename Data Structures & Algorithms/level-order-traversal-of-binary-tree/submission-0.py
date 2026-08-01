# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def traverse(root, depth):
            if not root:
                return

            if len(ans) == depth:
                ans.append([])

            ans[depth].append(root.val)
            
            traverse(root.left, depth + 1)
            traverse(root.right, depth + 1)
        traverse(root, 0)
        return ans