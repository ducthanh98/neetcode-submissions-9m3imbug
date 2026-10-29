class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        res_start = 0

        def expand(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1 
                r += 1
            return r - l - 1

        for i in range(len(s)):
            a = expand(i,i)
            b = expand(i, i+1)
            curr_len = max(a,b)
            if curr_len > res:
                res = curr_len
                res_start = i - (curr_len - 1) // 2

        return s[res_start : res_start + res]
            

