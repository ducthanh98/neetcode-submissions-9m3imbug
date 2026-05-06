# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countGoodNodes(self,root: TreeNode, max_cur_path: int):
        if not root:
            return 0
        cur = 0
        if root.val >= max_cur_path:
            max_cur_path = root.val
            cur = 1 
        left = self.countGoodNodes(root.left, max_cur_path)
        right = self.countGoodNodes(root.right,max_cur_path)
        return left + right  + cur


    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countGoodNodes(root, float('-inf'))
        
