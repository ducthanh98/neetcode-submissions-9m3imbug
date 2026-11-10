class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)
        
        # Nếu tổng độ dài không khớp thì chắc chắn False
        if m + n != l:
            return False
            
        # Tạo bảng DP kích thước (m + 1) x (n + 1)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Trạng thái cơ sở: hai chuỗi rỗng tạo thành chuỗi rỗng
        dp[0][0] = True
        
        # Điền hàng đầu tiên (chỉ dùng s2)
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
            
        # Điền cột đầu tiên (chỉ dùng s1)
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
            
        # Điền phần còn lại của bảng
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                from_s1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                from_s2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[i][j] = from_s1 or from_s2
                
        return dp[m][n]