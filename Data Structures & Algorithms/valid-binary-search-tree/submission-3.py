# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkBST(node: Optional[TreeNode], low: float, high: float) -> bool:
            # Nếu node rỗng thì luôn đúng
            if not node:
                return True
            
            # Giá trị node hiện tại phải nằm TRONG khoảng (low, high)
            # Lưu ý: BST không cho phép giá trị bằng nhau (tùy định nghĩa, nhưng LeetCode thường là vậy)
            if not (low < node.val < high):
                return False
            
            # Khi sang trái: Giá trị lớn nhất có thể đạt được là node.val
            # Khi sang phải: Giá trị nhỏ nhất có thể đạt được là node.val
            return (checkBST(node.left, low, node.val) and 
                    checkBST(node.right, node.val, high))

        # Khởi tạo với khoảng âm vô cực đến dương vô cực
        return checkBST(root, float('-inf'), float('inf'))


        
        