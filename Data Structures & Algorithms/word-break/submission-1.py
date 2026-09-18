class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def dp(i):
            if i == len(s):
                return True
            if i in cache:
                return cache[i]
            for w in wordDict:
                if s[i:i + len(w)] == w and dp(i + len(w)):
                    cache[i] = True  
                    return True
            cache[i] = False
            return False

        return dp(0)