class Solution:
    def minWindow(self, s: str, t: str) -> str:
        state = {}
        for v in t:
            state[v] = state.get(v,0) + 1
        count = len(t)
        min_length = 999999
        res = ""
        l,r = 0,0
        while(r < len(s)):
            print(state, 'count',count,'r', l, r ,'length',len(s))
            if(s[r] in state):
                if(state[s[r]] > 0): 
                    count -=1
                state[s[r]] -= 1
            while(count == 0):
                print('count == 0', l , r, state)
                if min_length > r - l + 1:
                    min_length = r - l + 1
                    res = s[l:r + 1]
                
                if(s[l] in state):
                    state[s[l]] += 1                        
                    if(state[s[l]] > 0):
                        count += 1

                l+= 1
            r += 1


        return res
            
            