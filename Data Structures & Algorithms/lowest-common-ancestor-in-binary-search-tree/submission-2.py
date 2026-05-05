# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 1. Base case: Nếu đi hết nhánh (None) hoặc chạm đúng p hoặc q
        if not root or root.val == p.val or root.val == q.val:
            return root

        # 2. Đệ quy tìm ở 2 phía
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 3. Tổng hợp kết quả (Post-order logic)
        if left and right:
            # Nếu bên trái thấy 1 node, bên phải thấy 1 node -> root là LCA
            return root
        
        # Nếu chỉ 1 bên thấy (hoặc không bên nào thấy), trả về cái thấy được đó
        # Cái này sẽ truyền dần p hoặc q (hoặc LCA đã tìm được) lên trên
        return left or right