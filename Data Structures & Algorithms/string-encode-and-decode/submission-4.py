class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += f"{length}#{s}"
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        last_idx = 0
        i = 0
        while(i < len(s)):
            v = s[i]
            if v == "#":
                prefix = s[last_idx:i]
                last_idx = last_idx + int(prefix) + len(prefix) + 1 
                print(prefix,i+1,last_idx)
                res.append(f"{s[i+1:last_idx]}")
                i = last_idx+1
            else:
                i += 1


        return res
