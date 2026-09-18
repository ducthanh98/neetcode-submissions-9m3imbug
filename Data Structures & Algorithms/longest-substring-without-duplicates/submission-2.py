class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,count = 0,0
        cache = {}
        for i,v in enumerate(s):
            if v in cache:
                exist = cache[v]
                while(l <= exist):
                    idx = s[l]
                    print('delete', idx, cache, i ,v,l)
                    del cache[idx]
                    l += 1
            cache[v] = i

            if i -l + 1 > count:
                count = i -l + 1
            
        return count