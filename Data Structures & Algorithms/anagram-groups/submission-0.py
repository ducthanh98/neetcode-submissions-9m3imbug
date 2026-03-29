class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        res = defaultdict(list)
        for v in strs:
            key = [0] * 26
            for c in v:
                key[ord(c) - ord('a')] += 1
            res[tuple(key)].append(v)
                

        return list(res.values())