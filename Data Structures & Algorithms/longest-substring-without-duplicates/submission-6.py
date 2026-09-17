class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_res = 0
        cache = {}

        length = len(s)
        l = 0 
        for r in range(length):
            if s[r] in cache:
                l = max(l,cache[s[r]] + 1)
            cache[s[r]] = r

            if r - l + 1  > max_res:
                max_res = r - l + 1 

        return max_res
            



        