class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        l,r = 0,len(nums) - 1

        while l < r :
            mid = (l + r)//2
            print(mid, l ,r,'mid',nums[mid], nums[l], nums[r] )
            if mid < r and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[l] <= nums[mid] :
                l = mid + 1
            else:
                r = mid 
        print(l,r)
        return nums[l]