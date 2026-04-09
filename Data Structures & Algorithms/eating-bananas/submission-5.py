
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # l bắt đầu từ 1, r là số lớn nhất trong piles
        l, r = 1, max(piles)
        
        while l < r:
            mid = (l + r) // 2
            
            # Tính tổng thời gian dùng Generator Expression để tối ưu memory
            times = sum(math.ceil(piles_i / mid) for piles_i in piles)
            
            if times <= h:
                # Nếu ăn kịp, thử tốc độ nhỏ hơn (về phía bên trái)
                r = mid
            else:
                # Nếu không kịp, phải tăng tốc độ lên
                l = mid + 1
        
        return l