# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        cache = {}

        first = inorder
        idx = 0
        self.pre_idx = 0
        for i,v in enumerate(inorder):
            cache[v] = i
        
        def process(l: int, r : int):
            if l > r: 
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1 
            mid_idx = cache[root_val]


            left = process(l, mid_idx - 1 )
            right = process(mid_idx + 1 , r )

            root = TreeNode(root_val,left,right)
            return root


        return process(0 , len(inorder) - 1 )

