# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        seen = []
        best = 0
        if not root:
            return 0
        
        seen.append((root, 1))
        while len(seen) != 0:
            current = seen.pop(0)
            current_node = current[0]
            current_depth = current[1]
            best = max(best, current_depth)
            if current_node.left != None:
                seen.append((current_node.left, current_depth + 1))
            
            if current_node.right != None:
                seen.append((current_node.right, current_depth + 1))
        return best