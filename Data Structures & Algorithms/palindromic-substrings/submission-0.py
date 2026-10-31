class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        length = len(s)

        def expand(i,j):
            count = 0
            while 0 <= i and j < length and s[i] == s[j]:
                count += 1
                i -= 1 
                j += 1
            
            return count

        for i in range(length):
            result += expand(i,i)
            result += expand(i, i + 1)
        return result

        