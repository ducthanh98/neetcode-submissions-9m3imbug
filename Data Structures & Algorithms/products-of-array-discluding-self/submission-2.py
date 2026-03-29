class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        multiply_res = 1
        for i,n in enumerate(nums):
            if n == 0:
                zero_count += 1
            else:
                multiply_res *= n
        
        res = []

        if zero_count > 1:
            return [0] * len(nums)

        for n in nums:
            if zero_count == 1 and n == 0:
                res.append(multiply_res)
            elif zero_count == 1 :
                res.append(0)
            else:
                res.append(int(multiply_res/n))
        return res