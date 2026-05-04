# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalance = True
        def calcHeight(root:Optional[TreeNode]) -> int:
            nonlocal isBalance
            if not root:
                return 0

            left = calcHeight(root.left)
            right = calcHeight(root.right)

            if abs(left - right) > 1 :
                isBalance = False
            return max(left,right) + 1 
            
        calcHeight(root)
        return isBalance