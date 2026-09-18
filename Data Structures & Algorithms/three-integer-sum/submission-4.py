class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cache = {}
        res = set()
        for i,n in enumerate(nums):
            cache[n] = i
        nums.sort()
        for i,n in enumerate(nums):
            sum = 0 - n 

            l,r = i +1, len(nums) - 1
            while(l < r):
                tmp = nums[l] + nums[r]
                #if tmp == sum and n == nums[l] and n == nums[r]:
                #    l += 1
                #    r -= 1 
                #    continue
                if tmp == sum:
                    res.add(tuple([n,nums[l],nums[r]]))
                    l += 1
                    r -= 1
                elif tmp > sum:
                    r -= 1
                elif tmp < sum:
                    l += 1
        return  [list(i) for i in res]