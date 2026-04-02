class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cache = {}
        l,r = 0,0
        res = 0
        max_count = 0
        while(r < len(s)):
            if s[r] in cache :
                cache[s[r]] += 1
            else:
                cache[s[r]] = 1 

            if cache[s[r]] > max_count:
                max_count = cache[s[r]]

            tmp = r - l + 1 - max_count

            
            if tmp > k:
                cache[s[l]] -= 1
                l += 1 
            else:
                if r - l + 1 > res:
                    res = r - l + 1
            r += 1 

        return res