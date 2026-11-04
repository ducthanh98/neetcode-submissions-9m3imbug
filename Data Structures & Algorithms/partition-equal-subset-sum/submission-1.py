class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        nums.sort()
        print(nums)
        for n in nums:
            sum += n 
        if sum % 2 == 1 :
            return False

        sum = sum / 2
        res = False

        def dp(idx,cur_sum):
            if cur_sum == sum:
                return True
            if cur_sum > sum:
                return False
            tmp = False
            for i in range(idx + 1, len(nums)):
                if dp(i, cur_sum + nums[i]):
                    return True

            return False
                

        return dp(0,0)