class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Kiểm tra chiều cao bên trái
            left_height = check_height(node.left)
            if left_height == -1:  # Đã phát hiện mất cân bằng ở dưới
                return -1
                
            # Kiểm tra chiều cao bên phải
            right_height = check_height(node.right)
            if right_height == -1: # Đã phát hiện mất cân bằng ở dưới
                return -1
            
            # Kiểm tra sự chênh lệch tại nút hiện tại
            if abs(left_height - right_height) > 1:
                return -1
            
            # Trả về chiều cao thực nếu vẫn cân bằng
            return max(left_height, right_height) + 1

        return check_height(root) != -1