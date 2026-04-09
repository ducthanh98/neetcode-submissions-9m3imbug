
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float('inf')
        piles.sort()

        l,r = 1, piles[-1] + 1
        while(l < r):
            mid = (l +r) //2
            times = sum([math.ceil(x / mid) for x in piles])
            print(l,r,mid, times)

            if times <= h:
                if mid <= res:
                    res = mid
                
                r = mid
                
            else:
                l = mid + 1
    


        return res