class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        l,r = 0,len(nums) - 1

        while l < r :
            mid = (l + r)//2

            if nums[r] < nums[mid] :
                l = mid + 1
            else:
                r = mid 
        return nums[l]