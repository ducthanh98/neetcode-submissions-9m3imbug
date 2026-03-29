class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        arr = []
        for n,c in hashMap.items():
            arr.append([c,n])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res