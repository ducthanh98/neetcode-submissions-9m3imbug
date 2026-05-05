# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q :
            return False
        elif p.val != q.val :
            return False

        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right,q.right)
        return left and right   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if root:
            if root.val == subRoot.val:
                is_same =  self.isSameTree(root,subRoot)
                if is_same:
                    return True
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right
        return False



