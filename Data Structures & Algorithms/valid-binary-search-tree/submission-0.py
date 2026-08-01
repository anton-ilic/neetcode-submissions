# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValidBSTR(root, largest_smallest, smallest_largest):
            if not root:
                return True
            
            if largest_smallest < root.val < smallest_largest:
                return isValidBSTR(root.left, largest_smallest, min(smallest_largest, root.val)) and isValidBSTR(root.right, max(largest_smallest, root.val), smallest_largest)
            else:
                return False
            
        return isValidBSTR(root, -float('inf'), float('inf'))

