from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(maxsize=None)
        def dfs(i: int, j: int) -> int:
            # Base case: nếu duyệt hết 1 trong 2 chuỗi
            if i == len(word1):
                return len(word2) - j  # Cần chèn phần còn lại của word2
            if j == len(word2):
                return len(word1) - i  # Cần xóa phần còn lại của word1
                
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
                
            return 1 + min(
                dfs(i + 1, j),      # Xóa word1[i]
                dfs(i, j + 1),      # Chèn ký tự giống word2[j] vào trước word1[i]
                dfs(i + 1, j + 1)   # Thay thế word1[i] bằng word2[j]
            )
            
        return dfs(0, 0)