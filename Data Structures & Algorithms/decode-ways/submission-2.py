class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)

        number_to_char = {str(i+1) : chr(ord('A') + i) for i in range(26)}
        cache = {}
        def dp(i):
            if i in cache:
                return cache[i]
            total = 0
            if i == length:
                return 1
            if i >= length:
                return 0
            if s[i:i+ 1] in number_to_char:
                total += dp(i + 1)

            if s[i:i +2] in number_to_char:

                total += dp(i+2)
            cache[i] = total
            return total
            
            
            
        return dp(0)