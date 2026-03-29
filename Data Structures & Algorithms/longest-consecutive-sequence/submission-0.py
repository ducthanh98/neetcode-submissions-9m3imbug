class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}
        for n in nums:
            hash_map[n] = 1
        res = 0
        cache = {}
        def calc_longest(i : int) -> int:
            nonlocal res
            if i not in hash_map:
                return 0
            if i in cache:
                return cache[i]
            
            tmp =  1 + calc_longest(i + 1)
            cache[i] = tmp
            if tmp > res:
                res = tmp
            return tmp

        for n in nums:
            calc_longest(n)
        return res
