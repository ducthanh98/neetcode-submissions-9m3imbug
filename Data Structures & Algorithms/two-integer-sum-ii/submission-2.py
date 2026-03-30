class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = {}
        for i,n in enumerate(numbers):
            cache[n] = i
        numbers.sort()
        print(numbers)
        for i,n in enumerate(numbers):
            remain = target - n
            if remain == n:
                continue
            if remain in cache:
                return [i + 1,cache[remain] + 1]
        return [0,0]