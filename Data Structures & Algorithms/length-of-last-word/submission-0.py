class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        is_start = False

        length = len(s) - 1
        is_start = False
        count = 0 
        while length >= 0 :
            idx = length
            length -= 1
            if s[idx] == " " and not is_start :
                continue
            elif s[idx] == " " and is_start:
                return count
            is_start = True
            count += 1

        return count
