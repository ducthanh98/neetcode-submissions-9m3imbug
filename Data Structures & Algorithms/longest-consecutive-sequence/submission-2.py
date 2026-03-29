from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Dùng set() để lookup O(1) nhanh hơn dict
        num_set = set(nums)
        res = 0
        cache = {}

        def calc_longest(i: int) -> int:
            nonlocal res # Cho phép sửa biến res của hàm cha
            
            if i not in num_set:
                return 0
            if i in cache:
                return cache[i]
            
            # Đệ quy tìm số tiếp theo
            tmp = 1 + calc_longest(i + 1)
            cache[i] = tmp
            
            if tmp > res:
                res = tmp
            return tmp

        for n in nums:
            # Nếu đã có trong cache thì không cần gọi hàm để tiết kiệm stack
            if n not in cache:
                calc_longest(n)
                
        return res