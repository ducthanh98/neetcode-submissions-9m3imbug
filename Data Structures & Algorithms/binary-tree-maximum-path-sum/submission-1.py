# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def gain_max(root: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if root is None:
                return 0

            left = max(gain_max(root.left), 0 )
            right = max(gain_max(root.right), 0 )

            tmp = root.val + left + right
            if tmp > max_sum:
                max_sum = tmp
            
            return root.val + max(left, right )

        gain_max(root)
        return max_sum


