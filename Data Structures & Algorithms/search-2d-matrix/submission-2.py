class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m,n = len(matrix), len(matrix[0])

        l,r = 0, m*n

        while l < r: 
            mid = (l + r) //2
            mid_val = matrix[mid // n][mid % n]
            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid + 1
            else:
                r = mid


        return False