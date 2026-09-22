from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh_count = 0
        
        maxr = len(grid)
        maxc = len(grid[0])
        
        # Bước 1: Đưa tất cả cam thối ban đầu vào hàng đợi, đồng thời đếm số cam tươi
        for r in range(maxr):
            for c in range(maxc):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        # Nếu không có cam tươi nào, tốn 0 phút
        if fresh_count == 0:
            return 0
            
        minutes = 0
        
        # Bước 2: BFS lây nhiễm từng phút
        while q and fresh_count > 0:
            length = len(q)
            
            # Xử lý toàn bộ các quả cam thối trong 1 phút hiện tại
            for _ in range(length):
                r, c = q.popleft() # Dùng popleft thay vì pop
                
                for i, j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    newr, newc = r + i, c + j
                    
                    # Nếu trong phạm vi và là CAM TƯƠI (1)
                    if 0 <= newr < maxr and 0 <= newc < maxc and grid[newr][newc] == 1:
                        grid[newr][newc] = 2 # Đánh dấu đã thối
                        fresh_count -= 1     # Giảm số lượng cam tươi
                        q.append((newr, newc))
            
            minutes += 1 # Hết 1 vòng (1 tầng) thì tăng 1 phút
            
        # Bước 3: Trả về kết quả
        # Nếu vẫn còn cam tươi -> Không lây hết được -> Trả về -1
        return minutes if fresh_count == 0 else -1