class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_product = nums[0]
        max_product = nums[0]
        result = nums[0]

        for i in range(1,len(nums)):
            num = nums[i]

            tmp = max(num, min_product * num , max_product * num)
            min_product = min(num, min_product * num , max_product * num)

            max_product = tmp
            result = max(result, max_product)

        return result