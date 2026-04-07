class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        # Thêm cột 0 vào cuối để ép stack pop hết các phần tử còn lại
        heights.append(0) 
        
        for idx, height in enumerate(heights):
            # Khi gặp cột thấp hơn cột ở đỉnh stack
            while stack and heights[stack[-1]] > height:
                mid_idx = stack.pop()
                h = heights[mid_idx]
                
                # Tính chiều rộng
                if not stack:
                    w = idx
                else:
                    w = idx - stack[-1] - 1
                
                res = max(res, h * w)
            
            # Sau khi pop hết các cột cao hơn, mới thêm cột hiện tại vào
            stack.append(idx)
            
        return res