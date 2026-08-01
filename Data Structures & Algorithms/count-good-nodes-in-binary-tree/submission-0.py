# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # root will always be good
        # any other one is good if it's seen doesnt have a bigger node
        def goodNodesR(current, highest):
            if not current:
                return 0
            
            if current.val < highest:
                return goodNodesR(current.left, highest) + goodNodesR(current.right, highest)
            
            highest = current.val
            return 1 + goodNodesR(current.left, highest) + goodNodesR(current.right, highest)

            
        return goodNodesR(root, root.val)